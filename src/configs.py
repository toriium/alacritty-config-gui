from typing import Literal, Union, TypeAlias
from dataclasses import dataclass, field


@dataclass
class BaseConfig:
    name: str
    default: bool | str


@dataclass
class ChoicesConfig(BaseConfig):
    choices: list[str] = field(default_factory=list)


@dataclass
class BooleanConfig(BaseConfig): ...


class StringConfig(BaseConfig): ...


class FilePickerConfig(BaseConfig): ...


ALL_CONFIGS: TypeAlias = StringConfig | BooleanConfig | ChoicesConfig | FilePickerConfig


class GeneralConfigs:
    working_directory = StringConfig(name="working_directory", default="$HOME")
    live_config_reload: BooleanConfig = BooleanConfig(name="live_config_reload", default=True)
    ipc_socket: BooleanConfig = BooleanConfig(name="ipc_socket", default=True)
