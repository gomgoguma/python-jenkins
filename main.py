import uvicorn
from fastapi import FastAPI, APIRouter
import py_eureka_client.eureka_client as eureka_client
from config.env import HOST, PORT, EUREKA_SERVER, EUREKA_APP_NAME

from notify.router import notify_router

app = FastAPI(docs_url='/api/notify/docs', redoc_url='/api/notify/redoc', openapi_url='/api/notify/openapi.json')

router = APIRouter()
app.include_router(notify_router.router, prefix="/api/notify")

if __name__ == "__main__":
    eureka_client.init(eureka_server=EUREKA_SERVER,
                       app_name=EUREKA_APP_NAME,
                       instance_host=HOST,
                       instance_port=int(PORT))

    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True, )
