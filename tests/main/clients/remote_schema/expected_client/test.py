from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class Test(BaseModel):
    test_query: Optional[int] = Field(alias="testQuery")


Test.update_forward_refs()
