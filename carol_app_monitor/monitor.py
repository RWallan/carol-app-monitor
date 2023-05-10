from typing import Dict, List

from .carol_api import (
    get_all_carol_app_names,
    get_entity_type,
    get_process_name,
    get_process_status,
    get_properties_from_app,
)
from .utils import filter_dicts_by_values, merge_dicts


def create_monitor_schema() -> List[Dict[str, str]]:
    """Create the monitor schema with:

    * App name;
    * Process status;
    * Process name;
    * Entity type.

    Returns:
        List[Dict[str, str]]: The list of dicts containing the monitor schema\
        with: `app_name`, `process_status`, `process_name`, `entity_type`.
    """
    properties = get_properties_from_app()

    app_names = get_all_carol_app_names(properties)

    process_statuses = get_process_status(app_names)
    process_names = get_process_name(app_names)
    entity_types = get_entity_type(app_names)

    temp_schema = []
    for process_status, process_name, entity_type in zip(
        process_statuses, process_names, entity_types
    ):
        merged_dict = merge_dicts(process_status, process_name, entity_type)

        temp_schema.append(merged_dict)

    monitor_schema = filter_dicts_by_values(temp_schema, None, drop=True)

    return monitor_schema
