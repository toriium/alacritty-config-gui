import flet as ft


class CheckboxComponent(ft.Checkbox):
    def __init__(self, label: str, value: bool = False):
        super().__init__(label=label, value=value)



class CodeBlock(ft.Container):
    def __init__(self, code: str = ""):
        super().__init__()

        # Control Parameters
        self.expand = True
        self.min_width = 350
        self.bgcolor = ft.Colors.GREY_700
        self.border = ft.Border.all(5, ft.Colors.BLUE_100)
        self.border_color = ft.Colors.GREEN
        self.border_radius = 8
        self.padding = 12


        self.code_text = ft.Text(
            value=code,
            color=ft.Colors.WHITE,
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

        self.content = scroll_view

    def set_code(self, code: str) -> None:
        self.code_text.value = code