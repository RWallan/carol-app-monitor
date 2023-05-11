import pytest

from carol_app_monitor import exceptions


def test_task_error_must_return_correct_message():
    with pytest.raises(exceptions.TaskError) as excinfo:
        raise exceptions.TaskError("my_task_id")

    assert (
        excinfo.value.message
        == "Something wrong while processing the task: my_task_id"
    )


def test_max_retry_error_must_return_correct_message():
    with pytest.raises(exceptions.MaxRetryError) as excinfo:
        raise exceptions.MaxRetryError(2)

    assert excinfo.value.message == "Exceeded maximum number of attempts (2)"
