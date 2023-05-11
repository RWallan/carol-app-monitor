from carol_app_monitor import main


def test_execute_monitor_calls_function_correctly(mocker):
    create_monitor_schema_mock = mocker.MagicMock()
    start_online_processes_mock = mocker.MagicMock()

    mocker.patch(
        "carol_app_monitor.main.monitor.create_monitor_schema",
        create_monitor_schema_mock,
    )
    mocker.patch(
        "carol_app_monitor.main.monitor.start_online_processes",
        start_online_processes_mock,
    )

    main.execute_monitor()

    create_monitor_schema_mock.assert_called_once_with()
    start_online_processes_mock.assert_called_once_with(
        create_monitor_schema_mock.return_value, num_retries=2
    )
