from carol_app_monitor import monitor


def test_create_monitor_schema_must_return_correct_schema():
    expected_monitor_schema = [
        {
            "app_name": "scloud1",
            "process_status": "PAUSED",
            "process_name": "docker_jupyter",
            "entity_type": "ONLINE",
        },
        {
            "app_name": "teste",
            "process_status": "PAUSED",
            "process_name": "versao2",
            "entity_type": "ONLINE",
        },
        {
            "app_name": "cargoappdemo",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "BATCH",
        },
        {
            "app_name": "aulas",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "BATCH",
        },
        {
            "app_name": "priappdemo",
            "process_status": "PAUSED",
            "process_name": "priapp",
            "entity_type": "ONLINE",
        },
        {
            "app_name": "carolappmonitor",
            "process_status": "PAUSED",
            "process_name": "carolappmonitor",
            "entity_type": "BATCH",
        },
    ]

    monitor_schema = monitor.create_monitor_schema()

    assert monitor_schema == expected_monitor_schema


def test_start_online_processes_must_return_correct_infos():
    monitor_schema = [
        {
            "app_name": "teste",
            "process_status": "PAUSED",
            "process_name": "versao2",
            "entity_type": "ONLINE",
        },
        {
            "app_name": "cargoappdemo",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "BATCH",
        },
        {
            "app_name": "aulas",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "BATCH",
        },
        {
            "app_name": "priappdemo",
            "process_status": "PAUSED",
            "process_name": "priapp",
            "entity_type": "ONLINE",
        },
    ]

    num_retries = 1

    expected_infos = [
        {
            "app_name": "teste",
            "status": {
                "success": "no",
                "detail": "MaxRetryError('Exceeded maximum number of attempts (1)')",
            },
        },
        {
            "app_name": "priappdemo",
            "status": {
                "success": "yes",
                "detail": "Task has successfully completed: AI Process: priapp START (Carol App: priappdemo)/<TASK_ID>",
            },
        },
    ]

    start_process_detail = monitor.start_online_processes(
        monitor_schema, num_retries
    )

    assert start_process_detail[0] == expected_infos[0]
    assert start_process_detail[1].get("status").get(
        "success"
    ) == expected_infos[1].get("status").get("success")
    assert len(start_process_detail) == 2
