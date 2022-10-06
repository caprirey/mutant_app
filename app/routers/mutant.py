from distutils.command.config import config
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.dynamodb_conn import put_item_db
from app.routers.mutant_core import *
from threading import Thread
from app.config import config

router = APIRouter()

class Payload(BaseModel):
    dna: list = []

@router.post("/mutant/", status_code=200)
async def get_body(payload: Payload):
    if invalid_data(payload.dna) == False:
        raise HTTPException(status_code=400, detail="Invalid data")
    is_mutant = search_x_gene(payload.dna,len(payload.dna))
    if is_mutant == False:        
        put_item_db(payload.json(),is_mutant)
        raise HTTPException(status_code=403, detail="You are not mutant")
    else:       
        target=put_item_db(payload.json(), is_mutant)        
    return {"result": "you have gene x"}