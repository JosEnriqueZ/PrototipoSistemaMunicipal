import flet as ft
 
#Card

def tarjeta(datos,informacion):
    tarjeta = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text(datos),
                        subtitle=ft.Text(informacion),
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width= 400,
            padding=20,
        )
    )

