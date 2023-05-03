from carol_app_monitor import carol_api


def test_get_properties_from_app_must_get_properties_from_all_existing_carol_apps():
    properties = carol_api.get_properties_from_app()

    assert len(properties.keys()) == 6
    assert properties.items() != {}


def test_get_all_carol_app_names_must_return_correctly_carol_app_names(
    properties,
):
    expected_data = [
        "scloud1",
        "teste",
        "cargoappdemo",
        "aulas",
        "priappdemo",
        "carolappmonitor",
    ]

    carol_app_names = carol_api.get_all_carol_app_names(properties)

    assert expected_data == carol_app_names


def test_get_process_status_must_return_correctly_carol_app_status_if_is_a_list_of_carol_apps():
    carol_apps = ["cargoappdemo", "priappdemo"]

    carol_apps_status = carol_api.get_process_status(carol_apps)

    assert carol_apps_status == [
        {"app_name": "cargoappdemo", "process_status": "PAUSED"},
        {"app_name": "priappdemo", "process_status": "PAUSED"},
    ]


def test_get_process_status_must_return_correctly_carol_app_status_if_is_a_unique_carol_app():
    carol_apps = "cargoappdemo"

    carol_apps_status = carol_api.get_process_status(carol_apps)

    assert carol_apps_status == [
        {
            "app_name": "cargoappdemo",
            "process_status": "PAUSED",
        }
    ]


def test_get_process_name_must_return_a_list_of_dict_containing_app_name_and_process_name_if_is_a_list_of_carol_apps():
    carol_apps = ["cargoappdemo", "priappdemo"]

    carol_apps_infos = carol_api.get_process_name(carol_apps)

    assert carol_apps_infos == [
        {"app_name": "cargoappdemo", "process_name": "cargoapp"},
        {"app_name": "priappdemo", "process_name": "priapp"},
    ]


def test_get_process_name_must_return_a_list_of_dict_containing_app_name_and_process_name_if_is_a_unique_of_carol_app():
    carol_apps = "cargoappdemo"

    carol_apps_infos = carol_api.get_process_name(carol_apps)

    assert carol_apps_infos == [
        {"app_name": "cargoappdemo", "process_name": "cargoapp"}
    ]


def test_start_process_must_return_task_id_and_success_status():
    app_info = {"app_name": "cargoappdemo", "process_name": "cargoapp"}

    task_info = carol_api.start_app_process(app_info)

    assert task_info.get("task_id") is not None
    assert task_info.get("success") == True


def test_get_task_status():
    task_status = carol_api.get_task_status("2d7b84d6834d4616a27dbd8c781f0320")

    assert task_status == "COMPLETED"
