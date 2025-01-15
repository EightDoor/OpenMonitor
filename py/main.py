from fastapi import FastAPI
from app import router, logger
from fastapi.middleware.cors import CORSMiddleware
from app.config import APP_RELOAD
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.init()
app.include_router(router.router)

if __name__ == "__main__":
    # TODO 生产环境关闭 reload=False    会影响CPU一直保持在30%
    uvicorn.run("main:app", host="0.0.0.0", port=8500, reload=APP_RELOAD)
