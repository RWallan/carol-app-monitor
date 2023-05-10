from carol_app_monitor import monitor


def test_create_monitor_schema_must_return_correct_schema():
    expected_monitor_schema = [
        {
            "app_name": "scloud1",
            "process_status": "PAUSED",
            "process_name": "docker_jupyter",
            "entity_type": "batch",
        },
        {
            "app_name": "teste",
            "process_status": "PAUSED",
            "process_name": "versao2",
            "entity_type": "online",
        },
        {
            "app_name": "cargoappdemo",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "batch",
        },
        {
            "app_name": "aulas",
            "process_status": "PAUSED",
            "process_name": "cargoapp",
            "entity_type": "batch",
        },
        {
            "app_name": "priappdemo",
            "process_status": "PAUSED",
            "process_name": "priapp",
            "entity_type": "online",
        },
    ]

    monitor_schema = monitor.create_monitor_schema()

    assert monitor_schema == expected_monitor_schema
