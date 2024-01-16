#importaciones
import flet as ft
from random import choice
from View.vistaMaquinaria import TabContentVistaMaquinaria
from View.vistaTrabajadores import TabContentVistaTrabajadores
from View.vistaFaenas import TabContentVistaFaenas
from View.vistaHome import TabcontentVistaHome

def main(page: ft.Page):
    page.title = "SISTEMA DE CONTROL Y SEGUIMIENTO DE MAQUINAS VEHICULOS Y EQUIPOS(SCS)"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = True
    page.window_height = 800
    page.update()

    # # Define una función que se llame cuando la ventana cambie de tamaño
    # def on_resize(event):
    #     # Cambia la altura de la página por la altura de la ventana
    #     page.height = event.window_height
    #     page.update()

    # # Asigna la función al evento on_resize de la página
    # page.on_resize = on_resize
    
    maquinariavista = TabContentVistaMaquinaria()
    maquinariatrabajador = TabContentVistaTrabajadores()
    maquinariafaena = TabContentVistaFaenas()
    maquinariahome = TabcontentVistaHome()

    page.add(

        ft.Tabs(
            expand=True,
            selected_index=0,
            tabs=[
                ft.Tab(
                    icon=ft.icons.HOME,
                    text="Home",
                    content=maquinariahome
                ),
                ft.Tab(
                    icon=ft.icons.DIRECTIONS_CAR_FILLED,
                    text="Maquinaria",
                    content=maquinariavista
                ),
                ft.Tab(
                    icon=ft.icons.PERSON,
                    text="Trabajadores",
                    content=maquinariatrabajador
                ),
                ft.Tab(
                    icon=ft.icons.BOOK,
                    text="Faenas",
                    content=maquinariafaena
                )
            ]
        ),
        ft.Text(
            "Hecho con amor ❤ por El Olimpus!",
            style=ft.TextThemeStyle.LABEL_SMALL,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color=ft.colors.BLUE_900,
        )

        
        # ft.Row(
        #     [
        #         todo,ft.VerticalDivider(width=1)
        #         #ft.Column([ todo], alignment=ft.MainAxisAlignment.START, expand=True)
        #     ],
        #     expand=True,
        # )
    )



    # page.add(todo)

ft.app(target=main)