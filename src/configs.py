from typing import Literal, Union, TypeAlias
from dataclasses import dataclass, field

@dataclass
class BaseConfig:
    name: str
    default: bool | str

@dataclass
class StringConfig(BaseConfig):
    options: list[str] = field(default_factory=list)

@dataclass
class BooleanConfig(BaseConfig):
    ...

ALL_CONFIGS: TypeAlias = StringConfig | BooleanConfig


class GeneralConfigs:
    working_directory: StringConfig = StringConfig(
        name="working_directory",
        options=["", "None"],
        default="$HOME"
    )
    live_config_reload: BooleanConfig = BooleanConfig(
        name="live_config_reload",
        default=True
    )
    ipc_socket : BooleanConfig = BooleanConfig(
        name="ipc_socket",
        default=True
    )