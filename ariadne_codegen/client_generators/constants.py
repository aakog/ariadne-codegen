from pathlib import Path
from typing import Dict

SIMPLE_TYPE_MAP: Dict[str, str] = {
    "String": "str",
    "ID": "str",
    "Int": "int",
    "Boolean": "bool",
    "Float": "float",
}
OPTIONAL: str = "Optional"
LIST: str = "List"
UNION: str = "Union"
ANY: str = "Any"
DICT = "Dict"
CALLABLE = "Callable"

TIMESTAMP_COMMENT = "# Generated by ariadne-codegen on {}\n"
SOURCE_COMMENT = "# Source: {}\n"
COMMENT_DATETIME_FORMAT = "%Y-%m-%d %H:%M"

BASE_MODEL_CLASS_NAME = "BaseModel"

TYPENAME_FIELD_NAME = "__typename"

TYPING_MODULE = "typing"
PYDANTIC_MODULE = "pydantic"
FIELD_CLASS = "Field"
UPDATE_FORWARD_REFS_METHOD = "update_forward_refs"
ENUM_MODULE = "enum"
ENUM_CLASS = "Enum"

MIXIN_NAME = "mixin"
MIXIN_FROM_NAME = "from"
MIXIN_IMPORT_NAME = "import"

SKIP_DIRECTIVE_NAME = "skip"
INCLUDE_DIRECTIVE_NAME = "include"

DEFAULT_ASYNC_BASE_CLIENT_PATH = (
    Path(__file__).parent / "dependencies" / "async_base_client.py"
)
DEFAULT_BASE_CLIENT_PATH = Path(__file__).parent / "dependencies" / "base_client.py"

GRAPHQL_CLIENT_EXCEPTIONS_NAMES = [
    "GraphQLClientError",
    "GraphQLClientHttpError",
    "GraphQlClientInvalidResponseError",
    "GraphQLClientGraphQLError",
    "GraphQLClientGraphQLMultiError",
]

SCALARS_PARSE_DICT_NAME = "SCALARS_PARSE_FUNCTIONS"
SCALARS_SERIALIZE_DICT_NAME = "SCALARS_SERIALIZE_FUNCTIONS"

UNSET = "UNSET"
UNSET_TYPE = "UnsetType"
