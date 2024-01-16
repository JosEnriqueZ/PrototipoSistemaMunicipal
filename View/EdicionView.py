import math
from flet import *
from datetime import datetime
from DB import conexion
from DB import TrabajadorService
import flet as ft

# the vista de trabajadores
class EdicionView(ft.UserControl):

    def __init__(self):
        super().__init__()
        

    def build(self):
        return ft.Column(
            [
                ft.Text("Trabajadores:", weight=ft.FontWeight.BOLD, size=20),
                ft.Row(
                    [
                        
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    [
                        self.mytabla   
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            #scroll=ft.ScrollMode.HIDDEN,
            spacing=20
        )

    

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(EdicionView())
    ft.app(main)