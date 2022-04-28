import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings

from app.api import router


app = FastAPI(title='API-шаблон',
              description='Шаблон для разработки api-доступа к проекту',
              version='1.0.0')

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
#     allow_credentials=True,
# )


app.include_router(router)

# @app.get("/")
# async def test():
#     return RedirectResponse(url="/docs/")


if __name__ == '__main__':
    uvicorn.run('main:app',
                host=settings.server_host,
                port=settings.server_port,
                reload=True, )
