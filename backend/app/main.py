from fastapi import FastAPI

from backend.app.api import router
from backend.app.core import config
from backend.app.core import services


app=FastAPI(title='F1 lab')

settings=config.get_settings()
app.state.services=services.build_services(settings)

app.include_router(router.router, prefix='/api/v1')



# @app.get('/health')
# def health():
#     return {'message': 'server is ready'}





