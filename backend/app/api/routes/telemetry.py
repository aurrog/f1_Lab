from fastapi import APIRouter


router=APIRouter(
    prefix=['/telemetry'],
    tags=['Telemetry']
)

@router.get('/', summary='Получить телеметрию пилота за гонку')
def get_telemetry():
    return {'message': 'service is working'}