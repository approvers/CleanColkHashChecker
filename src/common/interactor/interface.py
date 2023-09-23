from abc import ABC

from pydantic import BaseModel

from src.common.libraries.pydantic.config import BaseFrozenConfig


class BaseInputData(BaseModel, ABC):
    class Config(BaseFrozenConfig):
        pass


class BaseOutputData(BaseModel, ABC):
    class Config(BaseFrozenConfig):
        pass
