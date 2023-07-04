from commands.common.docker_helpers import get_docker_containers_by_name, Container
from commands.common.function_tags import tag, get_functions_by_tags, get_all_tags

from typing import List, Callable, Any
from multiprocessing import Pool, TimeoutError
import subprocess
import sys

MAX_TEST_RUNTIME = 10 * 60


@tag("test", "unit", "airflow")
def airflow_unit_tests() -> int:
    """
    Runs airflow unit tests. Returns exit code
    These tests are run inside the container because the airflow setup is very complicated and error prone manually.
    """
    print("Airflow unit tests:")
    matching_containers = get_docker_containers_by_name(
        "airflow-webserver", filter_by_project_name=True
    )
    assert (
        len(matching_containers) == 1
    ), f"There should be exactly one airflow-webserver container in this project. Found {len(matching_containers)}"
    container = matching_containers[0]

    return __run_command_in_container(container, "pytest")


@tag("test", "integration", "airflow")
def airflow_integration_tests() -> int:
    """
    Runs airflow integration tests, returns exit code
    """
    print("Airflow integration tests:")

    matching_containers = get_docker_containers_by_name(
        "airflow-webserver", filter_by_project_name=True
    )
    assert (
        len(matching_containers) == 1
    ), f"There should be exactly one airflow-webserver container in this project. Found {len(matching_containers)}"
    container = matching_containers[0]

    return __run_command_in_container(container, "airflow tasks test airflow_integration_test run")


@tag("test", "unit", "commands")
def commands_unit_tests() -> int:
    """
    Runs unit tests for commands and stack management. Returns exit code.
    """
    print("Commands unit tests")
    return subprocess.run(["pytest", "commands/common/tests.py"]).returncode


def __run_command_in_container(container: Container, command: str) -> int:
    """
    Runs a command inside a given docker container and returns the exit code

    :param container: Container object. Should come from the docker client library or docker_helpers.
    :param command: Command to be executed.
    :return: exit code
    """
    exit_code, output = container.exec_run(command)
    print(output.decode())
    return exit_code


def __test_runner(tests: List[Callable], num_workers: int = 1) -> int:
    """
    Runs tests and returns the maximum error code from among all tests run
    """
    print(f"tests: {[x.__name__ for x in tests]}")

    with Pool(processes=num_workers) as pool:
        exit_codes = pool.map(__function_caller, tests)
        print(f"exit_codes = {exit_codes}")
        return max(exit_codes)


def __function_caller(x: Callable) -> Any:
    return x()


def run() -> None:
    allowed_tags = get_all_tags()

    if "-h" in sys.argv or "--help" in sys.argv:
        print(
            f"""    Usage: python3 cli.py [test_suites ..]

    If test_suite is "all", or not supplied, all tests will run.
    Otherwise, test_suite should be one or more of the following: {allowed_tags}
"""
        )
        exit(0)

    requested_tests = sys.argv[1:]
    if requested_tests and "all" not in requested_tests:
        # Case where we run a subset of tests
        tests = get_functions_by_tags(*requested_tests)
    else:
        # Case where we run all tests
        tests = get_functions_by_tags("test")  # All tests should be tagged with test

    exit(__test_runner(list(tests), 4))
