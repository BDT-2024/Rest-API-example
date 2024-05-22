from pydantic import BaseModel


class Trainer(BaseModel):
    first_name: str
    last_name: str
    avg_defense: float
    avg_attack: float
