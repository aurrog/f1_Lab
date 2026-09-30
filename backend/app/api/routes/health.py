from fastapi import APIRouter


router=APIRouter(prefix='/health',
                 tags=['System'],
                 )


@router.get('/')
def health():
    return {'message': 'Service is working'}

