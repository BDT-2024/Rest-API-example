from abc import ABC, abstractmethod

from redis import Redis

from data_model.trainer import Trainer


class TrainerDao(ABC):

    @abstractmethod
    def save_trainer(self, trainer: Trainer) -> None:
        pass

    @abstractmethod
    def get_trainer(self, first_name: str, last_name: str) -> Trainer | None:
        pass


class TrainerRedisDao(TrainerDao):

    def __init__(self, host: str, port: int, db: int):
        self.conn = Redis(host=host, port=port, db=db)

    def save_trainer(self, trainer: Trainer) -> None:
        self.conn.set(f"{trainer.first_name}:{trainer.last_name}", trainer.json())

    def get_trainer(self, first_name: str, last_name: str) -> Trainer | None:
        raw_trainer = self.conn.get(f"{first_name}:{last_name}")
        if raw_trainer is None:
            return None

        trainer = Trainer.parse_raw(raw_trainer)

        return trainer

