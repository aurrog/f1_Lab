import pytest
from pydantic import ValidationError

from backend.app.models import queries



def test_positive_year_is_accepted():
    query = queries.RacesQuery(year=2000)

    assert query.year == 2000


@pytest.mark.parametrize('year', [0, -1, 'abc'])
def test_invalid_year_is_rejected(year):
    with pytest.raises(ValidationError):
        queries.RacesQuery(year=year)


def test_positive_session_key_is_accepted():
    query=queries.DriversQuery(session_key=11243)

    assert query.session_key==11243


@pytest.mark.parametrize('session_key', [0, -1, 'abc'])
def test_invalid_year_is_rejected(session_key):
    with pytest.raises(ValidationError):
        queries.DriversQuery(session_key=session_key)


