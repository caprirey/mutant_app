from fastapi import APIRouter, HTTPException
from app.db.dynamodb_conn import get_data_mutant_rows
from app.routers.mutant_core import *

router = APIRouter()

@router.get("/stats", status_code=200)
async def get_stats():
    mutant,total = get_data_mutant_rows()
    humans = int(total-mutant)

    if total == 0 or humans == 0:
        return { "detail": "There is no information"}        
    return { "count_mutant_dna": mutant, "count_human_dna": humans, "ratio": round((mutant/humans),1)}