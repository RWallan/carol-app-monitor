class TaskError(Exception):
    """Custom exception to handling task errors.

    Args:
        task_id (str): TaskID.
    """

    def __init__(self, task_id: str) -> None:
        self.message = f"Something wrong while processing the task: {task_id}"


class MaxRetryError(Exception):
    """Custom exception to handling max retry errors.

    Args:
        max_retries (int): Max retries.
    """

    def __init__(self, num_retries: int) -> None:
        self.message = f"Exceeded maximum number of attempts ({num_retries})"
