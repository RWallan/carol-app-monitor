class TaskError(Exception):
    """Custom exception to handling task errors.

    Args:
        task_id (str): TaskID.
    """

    def __init__(self, task_id: str) -> None:
        self.task_id = task_id
        self.args = (
            f"Something wrong while processing the task: {self.task_id}",
        )


class MaxRetryError(Exception):
    """Custom exception to handling max retry errors.

    Args:
        max_retries (int): Max retries.
    """

    def __init__(self, num_retries: int) -> None:
        self.num_retries = num_retries
        self.args = (
            f"Exceeded maximum number of attempts ({self.num_retries})",
        )
