import math
from flet import *
from datetime import datetime
from DB import conexion
from DB import TrabajadorService
import flet as ft

# the vista de trabajadores
class TabContentVistaTrabajadores(ft.UserControl):

    def __init__(self):
        super().__init__()
        
        self.fila_editar = None
        #text field nombre
        self.field_name = ft.TextField(
            label="Nombre",
            hint_text="Ingrese su nombre",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text field apellido
        self.field_apellido = ft.TextField(
            label="Apellido",
            hint_text="Ingrese su apellido",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Fecha Nacimiento
        self.field_fechaNac = ft.TextField(
            label="Fecha Nacimiento",
            hint_text="DD-MM-YYYY",
            value="",
            on_change=self.validar_fecha,
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Numero de Telefono
        self.field_numeroCel = ft.TextField(
            label="Numero de Celular",
            hint_text="Ingrese su numero de celular",
            value="",
            on_change=self.validar_numeros,
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
            on_change=self.validar_numeros,
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

        self.boton_guardar= ft.FilledButton(
                            "Guardar",
                            icon=ft.icons.SAVE,
                            on_click=self.CapturaDatos
                        )
        self.boton_editar=ft.FilledButton(
                            "Editar",
                            visible=False,
                            icon=ft.icons.SAVE,
                            on_click=self.CapturaDatos
                        )
        self.boton_limpiar=ft.FilledButton(
                            "Limpiar",
                            icon=ft.icons.DELETE,
                            on_click=self.LimpiarDatos
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
        self.mytabla.rows.clear()
        trabajadores = TrabajadorService.todos_trabajadores(conexion.conectar())
        for trabajador in trabajadores:
            def cargaEditar(trabajador):
                return lambda e: self.cargarDatos(trabajador)
            def eliminar(trabajador):
                return lambda e: self.eliminarDatos(trabajador)
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
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(trabajador))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(trabajador))),
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
                        self.boton_guardar,
                        self.boton_editar,
                        self.boton_limpiar
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

    def cargarDatos(self, trabajador):
        self.fila_editar = trabajador[0]
        self.field_name.value = trabajador[2]
        self.field_apellido.value = trabajador[3]
        fecha_str = trabajador[4].strftime("%d-%m-%Y")
        self.field_fechaNac.value = fecha_str
        self.field_numeroCel.value = trabajador[5]
        self.field_traba.value = trabajador[6]
        self.field_numeroDNI.value = trabajador[7]
        self.field_direccion.value = trabajador[8]
        self.field_licencia.value = trabajador[9]
        self.boton_guardar.visible=False
        self.boton_editar.visible=True
        self.update()

    def eliminarDatos(self, trabajador):
        # Encuentra la fila que contiene los datos del trabajador
        selected_row = next(row for row in self.mytabla.rows if row.cells[0].content.value == trabajador[2])
        # Elimina esta fila de la tabla
        self.mytabla.rows.remove(selected_row)

        TrabajadorService.eliminar_registro_trabajador(conexion.conectar(), trabajador[0])
        conexion.cerrar_conexion(conexion.conectar())
        # Actualiza la página para reflejar los cambios
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
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
        self.boton_guardar.visible=True
        self.boton_editar.visible=False

        if self.fila_editar is not None:
            self.mytabla.rows[self.fila_editar-1].cells[0].content.value = self.field_name.value
            self.mytabla.rows[self.fila_editar-1].cells[1].content.value = self.field_apellido.value
            self.mytabla.rows[self.fila_editar-1].cells[2].content.value = self.field_fechaNac.value
            self.mytabla.rows[self.fila_editar-1].cells[3].content.value = self.field_numeroCel.value
            self.mytabla.rows[self.fila_editar-1].cells[4].content.value = self.field_traba.value
            self.mytabla.rows[self.fila_editar-1].cells[5].content.value = self.field_numeroDNI.value
            self.mytabla.rows[self.fila_editar-1].cells[6].content.value = self.field_direccion.value
            self.mytabla.rows[self.fila_editar-1].cells[7].content.value = self.field_licencia.value

            fecha = datetime.strptime(self.field_fechaNac.value, "%d-%m-%Y")
            TrabajadorService.actualizar_registro_Trabajador(conexion.conectar(), 1, self.field_name.value, self.field_apellido.value, fecha, self.field_numeroCel.value, self.field_traba.value, self.field_numeroDNI.value, self.field_direccion.value, self.field_licencia.value,(self.fila_editar))
            conexion.cerrar_conexion(conexion.conectar())
            self.mytabla.rows.clear()
            trabajadores = TrabajadorService.todos_trabajadores(conexion.conectar())
            for trabajador in trabajadores:
                def cargaEditar(trabajador):
                    return lambda e: self.cargarDatos(trabajador)
                def eliminar(trabajador):
                    return lambda e: self.eliminarDatos(trabajador)
                self.mytabla.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(trabajador[2])),
                            DataCell(Text(trabajador[3])),
                            DataCell(Text(self.field_fechaNac.value)),
                            DataCell(Text(trabajador[5])),
                            DataCell(Text(trabajador[6])),
                            DataCell(Text(trabajador[7])),
                            DataCell(Text(trabajador[8])),
                            DataCell(Text(trabajador[9])),
                            DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(trabajador))),
                            DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(trabajador))),
                        ]
                    )
                )
                self.update()
            trabajadores = TrabajadorService.todos_trabajadores(conexion.conectar())
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            fecha = datetime.strptime(self.field_fechaNac.value, "%d-%m-%Y")
            TrabajadorService.crear_registro_trabajador(conexion.conectar(), 1, self.field_name.value, self.field_apellido.value, fecha, self.field_numeroCel.value, self.field_traba.value, self.field_numeroDNI.value, self.field_direccion.value, self.field_licencia.value)
            conexion.cerrar_conexion(conexion.conectar())
            self.mytabla.rows.clear()
            trabajadores = TrabajadorService.todos_trabajadores(conexion.conectar())
            for trabajador in trabajadores:
                def cargaEditar(trabajador):
                    return lambda e: self.cargarDatos(trabajador)
                def eliminar(trabajador):
                    return lambda e: self.eliminarDatos(trabajador)
                self.mytabla.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(trabajador[2])),
                            DataCell(Text(trabajador[3])),
                            DataCell(Text(self.field_fechaNac.value)),
                            DataCell(Text(trabajador[5])),
                            DataCell(Text(trabajador[6])),
                            DataCell(Text(trabajador[7])),
                            DataCell(Text(trabajador[8])),
                            DataCell(Text(trabajador[9])),
                            DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(trabajador))),
                            DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(trabajador))),
                        ]
                    )
                )
                self.update()
            # Si no se está editando ninguna fila, agrega una nueva fila
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(self.field_name.value)),
                        DataCell(Text(self.field_apellido.value)),
                        DataCell(Text(self.field_fechaNac.value)),
                        DataCell(Text(self.field_numeroCel.value)),
                        DataCell(Text(self.field_traba.value)),
                        DataCell(Text(self.field_numeroDNI.value)),
                        DataCell(Text(self.field_direccion.value)),
                        DataCell(Text(self.field_licencia.value)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE)),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED)),
                    ]
                
                )
            )
        self.update()
    #Validaciones
    def validar_nombre(self, e: ft.ControlEvent):
            # Verifica si el valor ingresado por el usuario contiene solo letras.
            if not e.control.value.isalpha():
                e.control.error_text = "Por favor, ingrese solo letras."
            else:
                e.control.error_text = ""
            self.update()
    
    def validar_numeros(self, e: ft.ControlEvent):
        # Verifica si el valor ingresado por el usuario contiene solo números.
        if not e.control.value.isdigit():
            e.control.error_text = "Por favor, ingrese solo números."
        else:
            e.control.error_text = ""
        self.update()

    def validar_fecha(self, e: ft.ControlEvent):
        # Verifica si el valor ingresado por el usuario es una fecha válida.
        fecha_str = e.control.value.strip()
        try:
            # Intenta convertir la cadena de texto a una fecha.
            datetime.strptime(fecha_str, "%d-%m-%Y")
            e.control.error_text = ""
        except ValueError:
            # Si la conversión falla, muestra un mensaje de error.
            e.control.error_text = "Por favor, ingrese una fecha válida en el formato DD-MM-YYYY."
        self.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaTrabajadores())
    ft.app(main)