from pytest import mark

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


def test_get_entity_type_must_return_a_list_of_dict_containing_app_name_and_entity_type_if_is_a_list_of_carol_apps():
    carol_apps = ["cargoappdemo", "priappdemo"]

    carol_apps_infos = carol_api.get_entity_type(carol_apps)

    assert carol_apps_infos == [
        {"app_name": "cargoappdemo", "entity_type": "BATCH"},
        {"app_name": "priappdemo", "entity_type": "ONLINE"},
    ]


def test_get_entity_type_must_return_a_list_of_dict_containing_app_name_and_entity_type_if_is_a_unique_carol_app():
    carol_apps = "cargoappdemo"

    carol_apps_infos = carol_api.get_entity_type(carol_apps)

    assert carol_apps_infos == [
        {"app_name": "cargoappdemo", "entity_type": "BATCH"},
    ]


@mark.parametrize(
    "task_id, task_name, expected",
    [
        (
            "a6c3e56de01749cbaca5d816d792fb00",
            "AI Process: priapp START (Carol App: priappdemo v1.0.0)",
            {
                "task_status": "CANCELED",
                "detail": "The task has been CANCELED: AI Process: priapp START (Carol App: priappdemo v1.0.0)/a6c3e56de01749cbaca5d816d792fb00",
            },
        ),
        (
            "2d7b84d6834d4616a27dbd8c781f0320",
            "TASK TEST",
            {
                "task_status": "COMPLETED",
                "detail": "Task has successfully completed: TASK TEST/2d7b84d6834d4616a27dbd8c781f0320",
            },
        ),
        (
            "06f7a61920e145ad98509e90f0fb54f0",
            "AI Process: versao2 START (Carol App: teste v1.0.0)",
            {
                "task_status": "FAILED",
                "detail": "Something went wrong while processing: AI Process: versao2 START (Carol App: teste v1.0.0)/06f7a61920e145ad98509e90f0fb54f0",
            },
        ),
        (
            "2d7b84d6834d4616a27dbd8c781f0320",
            "",
            {
                "task_status": "COMPLETED",
                "detail": "Task has successfully completed: 2d7b84d6834d4616a27dbd8c781f0320",
            },
        ),
    ],
)
def test_check_task_status_must_return_correct_info(
    task_id, task_name, expected
):
    task_info = carol_api.check_task_status(task_id, task_name)

    assert task_info == expected
