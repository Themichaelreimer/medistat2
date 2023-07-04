import os
import random, string

PASSWORD_LENGTH = 32


def run() -> None:
    """
    Generates a .env file in the project root.
    """
    if os.path.exists(".env"):
        if input("A .env file already exists - are you sure you want to continue? (Y/n)") != "Y":
            exit(0)

    env_vars = generate_env_vars()
    write_env_file(env_vars)


def generate_random_string(length: int, allow_symbols: bool = False) -> str:
    """
    Generates a random string of the given length
    Used for generating random passwords that get passed to docker containers
    """
    charset = string.ascii_letters + string.digits
    if allow_symbols:
        # Want to avoid a few special chars that would create escaping challenges
        charset += "!@#%^&*()~|,.;:=-+_[]"
    return "".join([random.choice(charset) for _ in range(length)])


def write_env_file(env_vars: dict) -> None:
    with open(".env", "w+") as file:
        file.write("# Warning: Do not edit this file directly. Edit generate_env.py instead\n")
        for key in env_vars:
            file.write(f'{key}="{env_vars[key]}"\n')


def generate_env_vars() -> dict[str, object]:
    result = {
        "HOST_NAME": "localhost",
        "BASE_DIR": os.getcwd(),  # Helps docker_compose out
        "AIRFLOW_UID": os.getuid(),  # Prevents permission errors with logs, etc
        "REDIS_PASS": generate_random_string(PASSWORD_LENGTH),
        "AIRFLOW_DB_PASS": generate_random_string(PASSWORD_LENGTH),
        "PROJECT_NAME": "medistat2",
    }
    return result
