import pytest
from pydantic import ValidationError

from backend.app.models import queries



def races_test_positive_year_is_accepted():
    query = queries.RacesQuery(year=2000)

    assert query.year == 2000


@pytest.mark.parametrize('year', [0, -1, 'abc'])
def races_test_invalid_year_is_rejected(year):
    with pytest.raises(ValidationError):
        queries.RacesQuery(year=year)


def drivers_test_positive_session_key_is_accepted():
    query=queries.DriversQuery(session_key=11243)

    assert query.session_key==11243


@pytest.mark.parametrize('session_key', [0, -1, 'abc'])
def drivers_test_invalid_year_is_rejected(session_key):
    with pytest.raises(ValidationError):
        queries.DriversQuery(session_key=session_key)


def laps_test_valid_params_is_accepted(session_key=2433, driver_number=12):
    query=queries.LapsQuery(session_key=session_key, driver_number=driver_number)

    assert query.session_key == session_key
    assert query.driver_number == driver_number


@pytest.mark.parametrize(['session_key', 'driver_number'], [[0, -1, 'abc'], [0, -1, 'abc']])
def laps_test_invalid_params_is_rejected(session_key, driver_number):
    query=queries.LapsQuery(session_key=session_key, driver_number=driver_number)

    assert query.session_key == session_key
    assert query.driver_number == driver_number

