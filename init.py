#importaciones
import os
import flet as ft
from DB import conexion
conexion

def main(page: ft.Page):
    page.title = "SISTEMA DE CONTROL Y SEGUIMIENTO DE MAQUINAS VEHICULOS Y EQUIPOS(SCS)"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    #Navegador
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DIRECTIONS_CAR_FILLED, 
                selected_icon=ft.icons.DIRECTIONS_CAR_FILLED, 
                label="Maquinarias"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PERSON),
                selected_icon_content=ft.Icon(ft.icons.PERSON),
                label="Trabajadores",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOK,
                selected_icon_content=ft.Icon(ft.icons.BOOK),
                label_content=ft.Text("Faenas"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    #imagen
    img = ft.Image(
        src=f"img/camion.png",
        width=1080,
        height=600,
        fit=ft.ImageFit.CONTAIN,
    )

    # Estrucutura principal del proyecto
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ img], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )



    # page.add(todo)

ft.app(target=main)