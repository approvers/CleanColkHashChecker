from typing import Literal

from pydantic.config import BaseConfig as PydanticBaseConfig, Extra


class ABCConfig(PydanticBaseConfig):
    validate_all = True
    validate_assignment = True
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"
    smart_union = True
    extra = Extra.forbid


class BaseConfig(PydanticBaseConfig):
    validate_all = True
    validate_assignment = True
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"
    smart_union = True
    extra = Extra.forbid


class BaseFrozenConfig(PydanticBaseConfig):
    validate_all = True
    allow_mutation = False
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"
    smart_union = True
    extra = Extra.forbid


class BaseConstantConfig(PydanticBaseConfig):
    frozen = True
    validate_all = True
    allow_mutation = False
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"
    smart_union = True
    extra = Extra.forbid
