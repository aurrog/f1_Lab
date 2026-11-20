import pytest
from pydantic import ValidationError

from backend.app.models import queries


def test_races_accepts_positive_year():
    query = queries.RacesQuery(year=2000)

    assert query.year == 2000


@pytest.mark.parametrize('year', [0, -1, 'abc'])
def test_races_rejects_invalid_year(year):
    with pytest.raises(ValidationError):
        queries.RacesQuery(year=year)


def test_drivers_accepts_positive_session_key():
    query = queries.DriversQuery(session_key=11243)

    assert query.session_key == 11243


@pytest.mark.parametrize('session_key', [0, -1, 'abc'])
def test_drivers_rejects_invalid_session_key(session_key):
    with pytest.raises(ValidationError):
        queries.DriversQuery(session_key=session_key)


def test_laps_accepts_valid_params():
    query = queries.LapsQuery(session_key=2433, driver_number=12)

    assert query.session_key == 2433
    assert query.driver_number == 12


@pytest.mark.parametrize(
    ('session_key', 'driver_number'),
    [(0, 12), (-1, 12), ('abc', 12), (2433, 0), (2433, -1), (2433, 'abc')],
)
def test_laps_rejects_invalid_params(session_key, driver_number):
    with pytest.raises(ValidationError):
        queries.LapsQuery(session_key=session_key, driver_number=driver_number)
