from unittest.mock import Mock

import pytest

from backend.storage.repository import Repository
from backend.app.services.races_service import RacesService
from backend.app.core.models import RepositoryQuery
from backend.app.integrations.openf1.client import OpenF1Client
from backend.app.models.queries import RacesQuery


@pytest.mark.parametrize('cached_data', [[{'session_key': 1}, {'session_key': 2}], []])
def test_cached_races_are_returned_without_api_request(cached_data):
    repository=Mock(spec=Repository)
    data_client=Mock(spec=OpenF1Client)

    repository.get.return_value=cached_data

    service=RacesService(data_client, repository)
    query=RacesQuery(year=2020)

    result=service.get_races(query)

    assert result==cached_data

    repository.get.assert_called_once_with(
        RepositoryQuery(
            query_type='get_races',
            year=2020,
        )
    )
    data_client.get_races.assert_not_called()
    repository.write.assert_not_called()


def test_missing_cache_loads_and_saves_races():
    repository=Mock(spec=Repository)
    data_client=Mock(spec=OpenF1Client)

    repository.get.return_value=None

    loaded_data=[{'session_key': 1}, {'session_key': 2}]
    data_client.get_races.return_value=loaded_data

    service=RacesService(data_client=data_client, repository=repository)
    query=RacesQuery(year=2020)

    result=service.get_races(query)

    assert result == loaded_data

    data_client.get_races.assert_called_once_with(2020)

    expected_key= RepositoryQuery(
        query_type='get_races',
        year=2020,
    ).get_id()

    repository.write.assert_called_once_with(
        expected_key,
        loaded_data
    )
