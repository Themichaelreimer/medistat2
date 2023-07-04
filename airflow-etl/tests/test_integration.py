from airflow.models import DagBag


def test_no_import_errors() -> None:
    bag = DagBag()
    dag = bag.get_dag(dag_id="airflow_integration_test")

    assert len(bag.import_errors) == 0
    assert dag is not None
