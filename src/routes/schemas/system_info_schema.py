from pydantic import BaseModel

from src.routes.schemas.common import COMMON_JSON_TYPE, FORBID_CONFIG_DICT


class SystemInfoCreateModel(BaseModel):
    data: COMMON_JSON_TYPE = None
    metadata: COMMON_JSON_TYPE = None
    model_config = FORBID_CONFIG_DICT
