import carol_app_monitor.carol_api as monitor


def test_get_properties_from_app_must_get_properties_from_all_existing_carol_apps():
    properties = monitor.get_properties_from_app()

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

    carol_app_names = monitor.get_all_carol_app_names(properties)

    assert expected_data == carol_app_names


def test_get_process_status_must_return_correctly_carol_app_status_if_is_a_list_of_carol_apps():
    carol_apps = ["cargoappdemo", "priappdemo"]

    carol_apps_status = monitor.get_process_status(carol_apps)

    assert carol_apps_status == {
        "cargoappdemo": "PAUSED",
        "priappdemo": "PAUSED",
    }


def test_get_process_status_must_return_correctly_carol_app_status_if_is_a_unique_carol_app():
    carol_apps = "cargoappdemo"

    carol_apps_status = monitor.get_process_status(carol_apps)

    assert carol_apps_status == {
        "cargoappdemo": "PAUSED",
    }
