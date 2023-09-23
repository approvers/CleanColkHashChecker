from pydantic import BaseModel

from src.common.libraries.pydantic.config import BaseConfig, BaseFrozenConfig, BaseConstantConfig


class ValueObjectModel(BaseModel):
    class Config(BaseFrozenConfig):
        pass


class FrozenValueObjectModel(BaseModel):
    class Config(BaseConstantConfig):
        pass


class EntityModel(BaseModel):
    class Config(BaseConfig):
        pass
