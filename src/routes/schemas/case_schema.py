from pydantic import BaseModel

from src.routes.schemas.common import FORBID_CONFIG_DICT


class CaseCreateModel(BaseModel):
    name: str
    model_config = FORBID_CONFIG_DICT


class CaseUpdateModel(BaseModel):
    name: str
    model_config = FORBID_CONFIG_DICT
