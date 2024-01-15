import math
from flet import *
from DB import conexion
from DB import TrabajadorService
import flet as ft

# the vista de trabajadores
class TabContentVistaTrabajadores(ft.UserControl):

    def __init__(self):
        super().__init__()
        #text field nombre
        self.field_name = ft.TextField(
            label="Nombre",
            hint_text="Ingrese su nombre",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text field apellido
        self.field_apellido = ft.TextField(
            label="Apellido",
            hint_text="Ingrese su apellido",
            value="",
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Fecha Nacimiento
        self.field_fechaNac = ft.TextField(
            label="Fecha Nacimiento",
            hint_text="DD-MM-YYYY",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Numero de Telefono
        self.field_numeroCel = ft.TextField(
            label="Numero de Celular",
            hint_text="Ingrese su numero de celular",
            value="",
            keyboard_type=ft.KeyboardType.NUMBER,

        )

        # text field Numero de Trabajador
        self.field_traba = ft.TextField(
            label="Trabajador",
            hint_text="Ingrese Rol del Trabajador",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Numero de DNI
        self.field_numeroDNI = ft.TextField(
            label="DNI",
            hint_text="Ingrese su DNI",
            value="",
            keyboard_type=ft.KeyboardType.NUMBER,

        )

        # text field Direccion
        self.field_direccion = ft.TextField(
            label="Direccion",
            hint_text="Ingrese su direccion",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field tipo Licencia Conducir
        self.field_licencia = ft.TextField(
            label="Categoria Licencia Conducir",
            hint_text="Ingrese su categoria de licencia de conducir",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        self.mytabla = ft.DataTable(
            border=ft.border.all(2, "black"),
            border_radius=10,
            width=1180,
            vertical_lines=ft.border.BorderSide(3, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            column_spacing=50,
            bgcolor="white",
            columns=[
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Apellido")),
                ft.DataColumn(ft.Text("Fecha Nacimiento")),
                ft.DataColumn(ft.Text("Numero Celular")),
                ft.DataColumn(ft.Text("Rol Trabajador")),
                ft.DataColumn(ft.Text("Numero DNI")),
                ft.DataColumn(ft.Text("Direccion")),
                ft.DataColumn(ft.Text("Licencia Conducir")),
                ft.DataColumn(ft.Text("Editar")),
                ft.DataColumn(ft.Text("ELiminar")),
            ],
            rows=[],
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_name,self.field_apellido],
                ),
                ft.Row(
                    [self.field_fechaNac,self.field_numeroCel],
                ),
                ft.Row(
                    [self.field_traba, self.field_numeroDNI],
                ),
                ft.Row(
                    [self.field_direccion, self.field_licencia],
                ),
                
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=11
        )
        #self.mytabla.rows.clear()
        trabajadores = TrabajadorService.todos_trabajadores(conexion.conectar())
        for trabajador in trabajadores:
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(trabajador[2])),
                        DataCell(Text(trabajador[3])),
                        DataCell(Text(trabajador[4])),
                        DataCell(Text(trabajador[5])),
                        DataCell(Text(trabajador[6])),
                        DataCell(Text(trabajador[7])),
                        DataCell(Text(trabajador[8])),
                        DataCell(Text(trabajador[9])),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE, on_click=self.cargarDatos)),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED)),
                    ]
                )
            )
        #self.update()
        return ft.Column(
            [
                ft.Text("Registro:", weight=ft.FontWeight.BOLD, size=20),
                all_fields,
                ft.Row(
                    [
                        ft.FilledButton(
                            "Guardar",
                            icon=ft.icons.SAVE,
                            on_click=self.CapturaDatos
                        ),
                        ft.FilledButton(
                            "Limpiar",
                            icon=ft.icons.DELETE,
                            on_click=self.LimpiarDatos
                        )
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
    
    def cargarDatos(self, e: ft.ControlEvent):
        print("hola")
        self.field_name.value ="hola"
        self.field_apellido.value = "hola"
        self.field_fechaNac.value = "hola"
        self.field_numeroCel.value = "hola"
        self.field_traba.value = "hola"
        self.field_numeroDNI.value = "hola"
        self.field_direccion.value = "hola"
        self.field_licencia.value = "hola"
        self.update()

    def LimpiarDatos(self, e: ft.ControlEvent):
        print("hola")
        self.field_name.value =""
        self.field_apellido.value = ""
        self.field_fechaNac.value = ""
        self.field_numeroCel.value = ""
        self.field_traba.value = ""
        self.field_numeroDNI.value = ""
        self.field_direccion.value = ""
        self.field_licencia.value = ""
        self.update()
    
    
    def CapturaDatos(self, e: ft.ControlEvent):
        """
        It updates the Icon object.
        :param e: The event object
        """
        print(self.field_name.value.strip())
        print(self.field_apellido.value.strip())
        print(self.field_fechaNac.value.strip())
        print(self.field_numeroCel.value.strip())
        print(self.field_traba.value.strip())
        print(self.field_numeroDNI.value.strip())
        print(self.field_direccion.value.strip())
        print(self.field_licencia.value.strip())


        self.mytabla.rows.append(
            DataRow(
                cells=[
                    DataCell(Text(self.field_name.value.strip())),
                    DataCell(Text(self.field_apellido.value.strip())),
                    DataCell(Text(self.field_fechaNac.value.strip())),
                    DataCell(Text(self.field_numeroCel.value.strip())),
                    DataCell(Text(self.field_traba.value.strip())),
                    DataCell(Text(self.field_numeroDNI.value.strip())),
                    DataCell(Text(self.field_direccion.value.strip())),
                    DataCell(Text(self.field_licencia.value.strip())),
                    DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE)),
                    DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED)),
                ]
            
            )
        )
        self.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaTrabajadores())
    ft.app(main)