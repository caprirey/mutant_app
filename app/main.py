from cgitb import handler
from fastapi import FastAPI
from app.routers import mutant,stats
from mangum import Mangum

app = FastAPI()

app.include_router(mutant.router, prefix="/api/v1")
app.include_router(stats.router, prefix="/api/v1")

handler = Mangum(app)