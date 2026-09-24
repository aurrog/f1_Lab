from fastapi import APIRouter


router=APIRouter()


@router.get('/')
def get_drivers():
    return [
        {'id': 1, 'name': 'Charles Leclerc'},
        {'id': 2, 'name': 'Lewis Hamilton'}
    ]

