import random
import time
from typing import Dict, List

from .carol_api import (
    check_task_status,
    get_all_carol_app_names,
    get_entity_type,
    get_process_name,
    get_process_status,
    get_properties_from_app,
    start_app_process,
)
from .exceptions import MaxRetryError, TaskError
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


def start_online_processes(
    monitor_schema: List[Dict[str, str]], num_retries: int = 2
) -> Dict[str, Dict[str, str]]:
    """Start all online processes that's not running.

    This function will filter online APPs from all CarolApps and check which\
    isn't running. To this cases, the `start_online_processes()` function\
    will try to start the process for `num_retries` explicited.

    Args:
        monitor_schema (List[Dict[str, str]]): The list of dicts containing\
        `app_name`, `process_status`, `process_name`, `entity_type`.

        num_retries (int, optional): Number of retries that function will\
            execute. Defaults to 2.

    Returns:
        Dict[str, Dict[str, str]]: The dictionary contaning the `app_name`,\
        `status`, `success` and `detail`
    """
    online_processes = filter_dicts_by_values(
        monitor_schema, "online", keep=True
    )
    not_running_processes = filter_dicts_by_values(
        online_processes, "RUNNING", drop=True
    )

    processes_status = []
    for process in not_running_processes:
        retry = 1
        app_name = process.get("app_name")
        process_name = process.get("process_name")
        try:
            process_info = start_app_process(process)
        except TaskError:
            try:
                time.sleep(round(12 * random.random() * 5, 2))
                process_info = start_app_process(process)
            except TaskError as error:
                process_status = {
                    "app_name": app_name,
                    "status": {"success": "no", "detail": repr(error)},
                }

                processes_status.append(process_status)
                break

        task_name = f"AI Process: {process_name} START (Carol App: {app_name})"
        task_info = check_task_status(process_info.get("task_id"), task_name)

        if task_info.get("task_status") != "COMPLETED":
            while retry <= num_retries:
                process_info = start_app_process(process)

                task_info = check_task_status(
                    process_info.get("task_id"), task_name
                )

                if task_info.get("task_status") == "COMPLETED":
                    break
                else:
                    time.sleep(round(12 * random.random() * 5, 2))
                    retry += 1

        if retry > num_retries:
            error = MaxRetryError(num_retries)

            process_status = {
                "app_name": app_name,
                "status": {"success": "no", "detail": repr(error)},
            }

            processes_status.append(process_status)

            continue

        process_status = {
            "app_name": app_name,
            "status": {"success": "yes", "detail": task_info.get("detail")},
        }

        processes_status.append(process_status)

    return processes_status
