import os
from pathlib import Path

import flet as ft


class CodeBlock(ft.Container):
    def __init__(self, code: str = ""):
        self.code_text = ft.Text(
            value=code,
            font_family="monospace",
            selectable=True,
            no_wrap=True,
        )

        # Scrollable viewport for large code content.
        scroll_view = ft.Column(
            controls=[self.code_text],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        super().__init__(
            content=scroll_view,
            expand=True,
            padding=10,
        )

    def set_code(self, code: str) -> None:
        self.code_text.value = code


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


class MainLayout(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True

        # Page elements
        self.code_block = CodeBlock(code="Empty")

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

        self.controls = [dropdown_configs, self.code_block]

    def on_dropdown_select(self, e):
        selected_key = e.control.value
        file_content = self.config_path_content.get(selected_key, "No content available")
        self.code_block.set_code(file_content)
        self.update()
