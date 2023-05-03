class TaskError(Exception):
    """Custom exception to handling task erros.

    Args:
        task_id (str): TaskID.
    """

    def __init__(self, task_id: str) -> None:
        self.message = f"Something wrong while processing the task: {task_id}"
