from fastapi import FastAPI
from app import router
import uvicorn

app = FastAPI()

app.include_router(router.router)

if __name__ == "__main__":
    # TODO 生产环境关闭 reload=False    会影响CPU一直保持在30%
    uvicorn.run("main:app", host="0.0.0.0", port=8500, reload=True)
