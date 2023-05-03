from typing import Any, Dict, List

from dotenv import find_dotenv, load_dotenv
from pycarol import Apps, Carol

_ = load_dotenv(find_dotenv(".env"))

carol = Carol()
apps = Apps(carol)


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


def get_process_status(app_name: str | List[str]) -> Dict[str, str]:
    """Get CarolApp process status by CarolApp name.

    Args:
        app_name (str | List[str]): CarolApp name. Can be `str` or a `list`.

    Returns:
        Dict[str, str]: A dict containing the CarolApp name and your process\
            status.
    """
    if isinstance(app_name, list):
        status = [
            apps.get_processes_info(app)
            .get("mdmTenantAppAIProcessValues")[0]
            .get("mdmRunningState")
            for app in app_name
        ]

        return {app: status for app, status in zip(app_name, status)}

    else:
        status = (
            apps.get_processes_info(app_name)
            .get("mdmTenantAppAIProcessValues")[0]
            .get("mdmRunningState")
        )

        return {app_name: status}
