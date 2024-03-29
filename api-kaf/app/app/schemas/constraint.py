from enum import Enum


class BaseEnum(Enum):
    """Base class for enumeration
    """
    @classmethod
    def has_value(cls, value: str | int) -> bool:
        return value in cls._value2member_map_

    @classmethod
    def get_values(cls) -> list[str | int]:
        return [e.value for e in cls]

    @classmethod
    def get_names(cls) -> list[Enum]:
        return [e for e in cls]


class BaseStrEnum(str, BaseEnum):
    """Base class for enumeration
    """
