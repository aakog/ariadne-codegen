from typing import Annotated, List, Literal, Union

from pydantic import Field

from .base_model import BaseModel


class ListInterface(BaseModel):
    query_list_i: List[
        Annotated[
            Union[
                "ListInterfaceQueryListIInterface",
                "ListInterfaceQueryListITypeA",
                "ListInterfaceQueryListITypeB",
            ],
            Field(discriminator="typename__"),
        ]
    ] = Field(alias="queryListI")


class ListInterfaceQueryListIInterface(BaseModel):
    typename__: Literal["Interface", "TypeC"] = Field(alias="__typename")
    id: str


class ListInterfaceQueryListITypeA(BaseModel):
    typename__: Literal["TypeA"] = Field(alias="__typename")
    id: str
    field_a: str = Field(alias="fieldA")


class ListInterfaceQueryListITypeB(BaseModel):
    typename__: Literal["TypeB"] = Field(alias="__typename")
    id: str
    field_b: str = Field(alias="fieldB")


ListInterface.update_forward_refs()
ListInterfaceQueryListIInterface.update_forward_refs()
ListInterfaceQueryListITypeA.update_forward_refs()
ListInterfaceQueryListITypeB.update_forward_refs()
