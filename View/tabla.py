#tabla
import flet as ft
   
tablaP = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("nombre")),
            ft.DataColumn(ft.Text("apellido")),
            ft.DataColumn(ft.Text("direccion")),
        ],
        rows=[],
    )