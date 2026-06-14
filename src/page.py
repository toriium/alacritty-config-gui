import os
from pathlib import Path

import flet as ft

from src.components.components import CheckboxComponent
from src.configs import ALL_CONFIGS, StringConfig, BooleanConfig, GeneralConfigs


def get_all_existing_configs():
    config_path_priorities = [
        "$XDG_CONFIG_HOME/alacritty/alacritty.toml",
        "$XDG_CONFIG_HOME/alacritty.toml",
        "$HOME/.config/alacritty/alacritty.toml",
        "$HOME/.alacritty.toml",
        "/etc/alacritty/alacritty.toml"
    ]

    paths = []
    for path in config_path_priorities:
        expanded_path = os.path.expandvars(path)
        if os.path.exists(expanded_path):
            paths.append(expanded_path)
    return paths


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def generate_config_controls(configs: list[ALL_CONFIGS]) -> list[ft.Control]:
    config_controls: list[ft.Control] = []
    for config in configs:
        if isinstance(config, BooleanConfig):
            control = CheckboxComponent(label=config.name, value=config.default)
        elif isinstance(config, StringConfig):
            control = ft.Dropdown(
                label=config.name,
                options=[ft.dropdown.Option(option) for option in config.options],
                value=config.default
            )
        else:
            raise Exception("Not implemented")

        config_controls.append(control)
    return config_controls


class MainLayout(ft.Column):
    def __init__(self):
        super().__init__()

        # Control Parameters
        self.expand = True

        # Page elements

        # Get config paths and their content
        self.config_path_content: dict[str, str] = {}
        for config_path in get_all_existing_configs():
            content = get_file_content(config_path)
            if content is not None:
                self.config_path_content[config_path] = content

        # Choices
        choices: list[ft.DropdownOption] = []
        choices = [ft.DropdownOption(key=path, text=Path(path).name) for path in self.config_path_content.keys()]

        dropdown_configs = ft.Dropdown(
            width=220,
            value="config_paths",
            options=choices,
            on_select=self.on_dropdown_select
        )

        # Config controls
        configs = [
            GeneralConfigs.working_directory,
            GeneralConfigs.live_config_reload,
            GeneralConfigs.ipc_socket
        ]
        config_controls = generate_config_controls(configs)

        self.controls = [
            dropdown_configs,
            *config_controls
        ]

    def on_dropdown_select(self, e):
        selected_key = e.control.value
        self.update()
