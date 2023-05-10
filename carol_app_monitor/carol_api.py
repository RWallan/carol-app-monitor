from typing import Any, Dict, List

from dotenv import find_dotenv, load_dotenv
from pycarol import Apps, Carol, Tasks

from carol_app_monitor.exceptions import TaskError

_ = load_dotenv(find_dotenv(".env"))

carol = Carol()
apps = Apps(carol)
tasks = Tasks(carol)


def get_properties_from_app() -> Dict[str, Dict[str, Any]]:
    """Get properties from all existing CarolApps in tenant ordered by date\
        created.

    Returns:
        Dict[str, Dict[str, Any]]: A dict with all properties from all\
            existing CarolApps.
    """
    return apps.all(entity_space="PRODUCTION", sort_by="mdmCreated")


def get_all_carol_app_names(
    properties: Dict[str, Dict[str, Any]]
) -> List[str]:
    """Get all CarolApp names existing in tenant.

    Args:
        properties (Dict[str, Dict[str, Any]]): A dict with properties from\
            CarolApps.

    Returns:
        List[str]: A list with all CarolApp names.
    """
    carol_app_names = list(properties.keys())
    return carol_app_names


def get_process_status(
    app_name: str | List[str],
) -> List[Dict[str, str | None]]:
    """Get CarolApp process status by CarolApp name.

    Args:
        app_name (str | List[str]): CarolApp name. Can be `str` or a `list`.

    Returns:
        List[Dict[str, str]]: A list of dicts containing the `app_name` and\
            your `process_status` or `None` if app doesn't have process infos.
    """
    if isinstance(app_name, list):
        _process_info = [apps.get_processes_info(app) for app in app_name]
        status = [
            process.get("mdmTenantAppAIProcessValues")[0].get(
                "mdmRunningState"
            )
            if process != {}
            else None
            for process in _process_info
        ]

        return [
            {"app_name": app, "process_status": status}
            for app, status in zip(app_name, status)
        ]

    else:
        _process_info = apps.get_processes_info(app_name)
        status = (
            _process_info.get("mdmTenantAppAIProcessValues")[0].get(
                "mdmRunningState"
            )
            if _process_info != {}
            else None
        )

        return [{"app_name": app_name, "process_status": status}]


def get_process_name(app_name: str | List[str]) -> List[Dict[str, str | None]]:
    """Get process name.

    Args:
        app_name (str | List[str]): CarolApp name. Can be `str` or a `list`.

    Returns:
        List[Dict[str, str]]: A list of dicts with `app_name` and the\
            `process_name` or `None` if app doesn't have process infos.
    """
    if isinstance(app_name, list):
        _process_info = [apps.get_processes_info(app) for app in app_name]
        process_names = [
            process.get("mdmTenantAppAIProcessValues")[0].get("mdmName")
            if process != {}
            else None
            for process in _process_info
        ]

        return [
            {"app_name": app, "process_name": process_name}
            for app, process_name in zip(app_name, process_names)
        ]
    else:
        _process_info = apps.get_processes_info(app_name)
        process_name = (
            _process_info.get("mdmTenantAppAIProcessValues")[0].get("mdmName")
            if _process_info != {}
            else None
        )

        return [{"app_name": app_name, "process_name": process_name}]


def start_app_process(app_info: Dict[str, str]) -> Dict[str, str]:
    """Start a CarolApp process.

    Args:
        app_info (Dict[str, str]): A dict containing the `app_name` and the\
            `process_name`.

    Raises:
        TaskError: If task fail, raises: Something wrong while processing the\
            task.

    Returns:
        Dict[str, str]: A dict with the `task_id` and the success status.
    """
    task_information = apps.start_app_process(
        app_info.get("process_name"), app_info.get("app_name")
    )

    task_id = task_information.get("data").get("mdmId")
    task_succeded = task_information.get("success")

    if not task_succeded:
        raise TaskError(task_id)

    return {"task_id": task_id, "success": task_succeded}


def get_task_status(task_id: str) -> str:
    """Check task status by `task_id`.

    Args:
        task_id (str): The TaskID.

    Returns:
        str: The task status. Can be: READY, RUNNING, COMPLETED, FAILED or\
            CANCELED.
    """
    return tasks.get_task(task_id).task_status


def get_entity_type(app_name: str | List[str]) -> List[Dict[str, str]]:
    """Get entity type from CarolApp by `app_name`.

    Args:
        app_name (str | List[str]): CarolApp name. Can be `str` or a `list`.

    Returns:
        List[Dict[str, str | None]]: A list of dicts with `app_name` and the\
            `entity_type`: `batch`, `online`, or `None` if app\
                doesn't have process infos.

    Notes:
        The `entity_type` can be:
        * mdmTenantAppAIProcess: batch
        * mdmTenantAppAIProcessWorking: online
    """
    TYPE_SCHEMA: Dict[str, str] = {
        "mdmTenantAppAIProcess": "batch",
        "mdmTenantAppAIProcessWorking": "online",
    }

    if isinstance(app_name, list):
        _process_info = [apps.get_processes_info(app) for app in app_name]
        _entity_types = [
            apps.get_processes_info(app).get("mdmEntityType")
            for app in app_name
        ]

        entity_types = [
            TYPE_SCHEMA.get(entity_type) for entity_type in _entity_types
        ]

        return [
            {"app_name": app, "entity_type": entity_type}
            for app, entity_type in zip(app_name, entity_types)
        ]
    else:
        _process_info = apps.get_processes_info(app_name)
        _entity_type = (
            _process_info.get("mdmEntityType") if _process_info != {} else None
        )

        entity_type = TYPE_SCHEMA.get(_entity_type)

        return [{"app_name": app_name, "entity_type": entity_type}]
