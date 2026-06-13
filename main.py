import flet as ft
from src.page import MainLayout



def main(page: ft.Page):

    page.title = "Alacritty Configs"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.DARK
    page.expand = True

    app_layout = MainLayout()
    page.add(app_layout)


ft.run(main=main)
