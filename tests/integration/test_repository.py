from backend.app.core.models import RepositoryQuery


def test_unknown_query_has_no_cache(repository):
    query = RepositoryQuery(
        query_type="get_drivers",
        session_key=9123,
    )

    assert repository.get(query) is None


def test_saved_drivers_can_be_loaded(repository):
    query = RepositoryQuery(
        query_type="get_drivers",
        session_key=9123,
    )
    data = [{"driver_number": 1}]

    repository.write(query.get_id(), data)
    result = repository.get(query)

    assert result == data
    