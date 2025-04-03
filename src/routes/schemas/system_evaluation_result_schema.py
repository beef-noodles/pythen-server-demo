from pydantic import BaseModel

from src.routes.schemas.common import COMMON_JSON_TYPE, FORBID_CONFIG_DICT


class SystemEvaluationResultCreateSchema(BaseModel):
    tag: str = None
    data: COMMON_JSON_TYPE = None
    summary: str = None
    model_config = FORBID_CONFIG_DICT


class SystemEvaluationResultQuerySchema(BaseModel):
    tag: str = None
    model_config = FORBID_CONFIG_DICT
