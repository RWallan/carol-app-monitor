import pytest

from carol_app_monitor.carol_api import get_properties_from_app


@pytest.fixture
def properties():
    return get_properties_from_app()
