from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.pessoas import router as pessoas_router
from app.db.database import criar_tabela
from app.core.logger import setup_logger

app = FastAPI()
criar_tabela()

setup_logger()

@app.get("/")
def home():
    return {"status:": "ok", "msg": "API rodando!"}


app.include_router(health_router)
app.include_router(pessoas_router) 

