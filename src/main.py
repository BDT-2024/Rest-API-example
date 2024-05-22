from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from data_model.trainer import Trainer
from redis_dao import TrainerRedisDao

app = FastAPI()


@app.post("/trainer/", response_model=Trainer)
async def create_person(trainer: Trainer):

    trainer_dao = TrainerRedisDao(host="localhost", port=6379, db=0)
    trainer_dao.save_trainer(trainer)

    return trainer


@app.get("/trainer/{first_name}/{last_name}", response_model=Trainer)
async def get_trainer(first_name: str, last_name: str):
    trainer_dao = TrainerRedisDao(host="localhost", port=6379, db=0)
    trainer = trainer_dao.get_trainer(first_name, last_name)

    if trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")

    return trainer
