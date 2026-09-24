from fastapi import FastAPI
from app

app=FastAPI()

app.include_router(
    
)

@app.get('/')
def hello_world():
    return {'message': 'Hello World!'}


@app.get('/health')
def health():
    return {'message': 'server is ready'}





