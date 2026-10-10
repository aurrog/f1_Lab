from unittest.mock import Mock

import pytest

from backend.app.core.models import RepositoryQuery
from backend.app.integrations.openf1.client import OpenF1Client
from backend.app.models.queries import DriversQuery
from backend.app.services.drivers_service import DriverService
from backend.storage.repository import Repository


@pytest.mark.parametrize('cached_data', [[{'driver_number': 1}], []])
def test_cached_drivers_are_returned_without_api_request(cached_data):
    repository = Mock(spec=Repository)
    data_client = Mock(spec=OpenF1Client)

    repository.get.return_value=cached_data

    service=DriverService(data_client, repository)
    query=DriversQuery(session_key=9123)

    result=service.get_drivers(query)

    assert result==cached_data

    repository.get.assert_called_once_with(
        RepositoryQuery(
            query_type="get_drivers",
            session_key=9123,
        )
    )
    data_client.get_drivers.assert_not_called()
    repository.write.assert_not_called()


def test_missing_cache_loads_and_saves_drivers():
    repository=Mock(spec=Repository)
    data_client=Mock(spec=OpenF1Client)

    repository.get.return_value=None

    loaded_data=[{'driver_number': 1}]
    data_client.get_drivers.return_value=loaded_data

    service=DriverService(data_client, repository)
    query=DriversQuery(session_key=11253)

    result = service.get_drivers(query)

    assert result == loaded_data

    data_client.get_drivers.assert_called_once_with(11253)

    expected_key= RepositoryQuery(
        query_type='get_drivers',
        session_key=11253,
    ).get_id()

    repository.write.assert_called_once_with(
        expected_key,
        loaded_data
    )