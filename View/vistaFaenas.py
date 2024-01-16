import math
from flet import *
from datetime import datetime
from DB import conexion
from Service import FaenaService
from Service import TrabajadorService
from Service import UsuarioService
from Service import VehiculoService
from Service import TipoVehiculoService
from Service import TipoCombustibleService

import flet as ft
# the content of the icon tab
class TabContentVistaFaenas(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.f_idvehiculo = None
        self.fila_editar = None
        self.selected_trabajador_id = None
        self.selected_Vehiculo_id = None
        
        #text field Trabajador
        self.field_trabajador = ft.TextField(
            label="Trabajador",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.trabajador_id_map = {}
        data = TrabajadorService.todos_trabajadores(conexion.conectar())
        self.items_Trabajador = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[2], checked=False, on_click=self.on_item_selected_TipoVehiculo) for d in data])
        for d in data:
            self.trabajador_id_map[d[2]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_Trabajador.items.append(ft.PopupMenuItem(text=d[2]))

        # text field Vehiculo
        self.field_vehiculo = ft.TextField(
            label="Vehiculo",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        self.vehiculo_id_map = {}
        data = VehiculoService.todos_Vehiculo(conexion.conectar())
        self.items_Vehiculo = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[12], checked=False, on_click=self.on_item_selected_TipoVehiculo) for d in data])
        for d in data:
            self.vehiculo_id_map[d[12]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_Trabajador.items.append(ft.PopupMenuItem(text=d[2]))
        
        # text field Fecha
        self.field_fecha = ft.TextField(
            label="Fecha",
            hint_text="DD-MM-YYYY",
            value="",
            on_change=self.validar_fecha,
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field Horas
        self.field_horas = ft.TextField(
            label="Horas",
            hint_text="Ingrese las horas",
            value="",
            on_change=self.validar_numeros,
            keyboard_type=ft.KeyboardType.NUMBER,

        )
        # text field Region
        self.field_region = ft.TextField(
            label="Region",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field Descripcion
        self.field_descripcion = ft.TextField(
            label="Descripcion",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field Direccion
        self.field_direccion = ft.TextField(
            label="Direccion",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field kilometros area
        self.field_kilometrosa = ft.TextField(
            label="Horas",
            hint_text="Ingrese los kilometros area",
            value="",
            on_change=self.validar_numeros,
            keyboard_type=ft.KeyboardType.NUMBER,

        )
        self.mytabla = ft.DataTable(
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            column_spacing=50,
            bgcolor="white",
            columns=[
                ft.DataColumn(ft.Text("Trabajador")),
                ft.DataColumn(ft.Text("Vehiculo")),
                ft.DataColumn(ft.Text("Fecha")),
                ft.DataColumn(ft.Text("Horas")),
                ft.DataColumn(ft.Text("Region")),
                ft.DataColumn(ft.Text("Descripcion")),
                ft.DataColumn(ft.Text("Direccion")),
                ft.DataColumn(ft.Text("Kilometros")),
                ft.DataColumn(ft.Text("Editar")),
                ft.DataColumn(ft.Text("Eliminar")),
            ],
            rows=[],
        )

        self.boton_guardar= ft.FilledButton(
                            "Guardar",
                            icon=ft.icons.SAVE,
                            on_click=self.EditaryGuardar
                        )
        self.boton_editar=ft.FilledButton(
                            "Editar",
                            visible=False,
                            icon=ft.icons.SAVE,
                            on_click=self.EditaryGuardar
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
                    [self.field_trabajador,self.items_Trabajador,self.field_vehiculo,self.items_Vehiculo],
                ),
                ft.Row(
                    [self.field_fecha,self.field_horas],
                ),
                ft.Row(
                    [self.field_region, self.field_descripcion],
                ),
                ft.Row(
                    [self.field_kilometrosa],
                ),
                
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=11
        )
        self.mytabla.rows.clear()
        faenas = FaenaService.todos_faenas(conexion.conectar())
        
        for vehiculo in faenas:
            def cargaEditar(vehiculo):
                return lambda e: self.cargarDatos(vehiculo)
            def eliminar(vehiculo):
                return lambda e: self.eliminarDatos(vehiculo)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(vehiculo[2])),
                        DataCell(Text(vehiculo[4])),
                        DataCell(Text(vehiculo[5])),
                        DataCell(Text(vehiculo[6])),
                        DataCell(Text(vehiculo[7])),
                        DataCell(Text(vehiculo[8])),
                        DataCell(Text(vehiculo[9])),
                        DataCell(Text(vehiculo[10])),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(vehiculo))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(vehiculo))),
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

    def cargarDatos(self, vehiculo):
        self.f_idvehiculo = vehiculo[0]
        self.selected_Vehiculo_id = vehiculo[1]
        self.selected_trabajador_id = vehiculo[2]
        self.fila_editar = vehiculo[0]
        # fecha_str = vehiculo[4].strftime("%d-%m-%Y")
        self.field_colorvehiculo.value = vehiculo[4]
        self.field_pesovehiculo.value = vehiculo[5]
        self.field_numerop.value = vehiculo[6]
        self.field_marca.value = vehiculo[7]
        self.field_año.value = vehiculo[8]
        self.field_revisiont.value = vehiculo[9]
        self.field_descripcion.value = vehiculo[10]
        self.boton_guardar.visible=False
        self.boton_editar.visible=True
        self.update()

    def eliminarDatos(self, vehiculo):
        # Encuentra la fila que contiene los datos del vehiculo
        selected_row = next(row for row in self.mytabla.rows if row.cells[0].content.value == vehiculo[12])
        # Elimina esta fila de la tabla
        self.mytabla.rows.remove(selected_row)
        # Actualiza la página para reflejar los cambios
        VehiculoService.eliminar_registro_Vehiculo(conexion.conectar(), vehiculo[0])
        conexion.cerrar_conexion(conexion.conectar())
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_tipovehiculo.value =""
        self.field_vehiculo.value = ""
        self.field_colorvehiculo.value = ""
        self.field_pesovehiculo.value = ""
        self.field_numerop.value = ""
        self.field_marca.value = ""
        self.field_año.value = ""
        self.field_revisiont.value = ""
        self.field_descripcion.value = ""
        self.field_galones.value = ""
        self.update()
    
    
    def EditaryGuardar(self, e: ft.ControlEvent):

        """Editar"""
        self.boton_guardar.visible=True
        self.boton_editar.visible=False

        if self.fila_editar is not None:
            self.mytabla.rows[self.fila_editar-1].cells[0].content.value = self.field_tipovehiculo.value
            self.mytabla.rows[self.fila_editar-1].cells[1].content.value = self.field_vehiculo.value
            self.mytabla.rows[self.fila_editar-1].cells[2].content.value = self.field_colorvehiculo.value
            self.mytabla.rows[self.fila_editar-1].cells[3].content.value = self.field_pesovehiculo.value
            self.mytabla.rows[self.fila_editar-1].cells[4].content.value = self.field_numerop.value
            self.mytabla.rows[self.fila_editar-1].cells[5].content.value = self.field_marca.value
            self.mytabla.rows[self.fila_editar-1].cells[6].content.value = self.field_año.value
            self.mytabla.rows[self.fila_editar-1].cells[7].content.value = self.field_revisiont.value
            self.mytabla.rows[self.fila_editar-1].cells[8].content.value = self.field_descripcion.value
            self.mytabla.rows[self.fila_editar-1].cells[9].content.value = self.field_galones.value
            
            #fecha = datetime.strptime(self.field_colorvehiculo.value, "%d-%m-%Y")
            VehiculoService.actualizar_registro_Vehiculo(conexion.conectar(), 1, 
                                                        self.selected_Vehiculo_id, 
                                                        self.selected_trabajador_id,
                                                        self.field_colorvehiculo.value, 
                                                        self.field_pesovehiculo.value, 
                                                        self.field_numerop.value, 
                                                        self.field_marca.value, 
                                                        self.field_año.value, 
                                                        self.field_revisiont.value,
                                                        self.field_descripcion.value,
                                                        self.field_galones.value,
                                                        self.f_idvehiculo)
            conexion.cerrar_conexion(conexion.conectar())
            self.mytabla.rows.clear()
            faenas = VehiculoService.todos_Vehiculo(conexion.conectar())
            for vehiculo in faenas:
                def cargaEditar(vehiculo):
                    return lambda e: self.cargarDatos(vehiculo)
                def eliminar(vehiculo):
                    return lambda e: self.eliminarDatos(vehiculo)
                self.mytabla.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(vehiculo[2])),
                            DataCell(Text(vehiculo[3])),
                            DataCell(Text(vehiculo[4])),
                            DataCell(Text(vehiculo[5])),
                            DataCell(Text(vehiculo[6])),
                            DataCell(Text(vehiculo[7])),
                            DataCell(Text(vehiculo[8])),
                            DataCell(Text(vehiculo[9])),
                            DataCell(Text(vehiculo[10])),
                            DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(vehiculo))),
                            DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(vehiculo))),
                        ]
                    )
                )
                # self.update()
            faenas = VehiculoService.todos_Vehiculo(conexion.conectar())
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
            self.update()
        else:

            """Guardar"""
            #fecha = datetime.strptime(self.field_colorvehiculo.value, "%d-%m-%Y")
            VehiculoService.crear_registro_Vehiculo(conexion.conectar(), 1, self.selected_Vehiculo_id, 
                                                    self.selected_trabajador_id,
                                                    self.field_colorvehiculo.value, 
                                                    self.field_pesovehiculo.value, 
                                                    self.field_numerop.value, 
                                                    self.field_marca.value, 
                                                    self.field_año.value, 
                                                    self.field_revisiont.value,
                                                    self.field_descripcion.value,
                                                    self.field_galones.value)
            conexion.cerrar_conexion(conexion.conectar())
            self.mytabla.rows.clear()
            faenas = VehiculoService.todos_Vehiculo(conexion.conectar())
            for vehiculo in faenas:
                def cargaEditar(vehiculo):
                    return lambda e: self.cargarDatos(vehiculo)
                def eliminar(vehiculo):
                    return lambda e: self.eliminarDatos(vehiculo)
                self.mytabla.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(vehiculo[12])),
                            DataCell(Text(vehiculo[13])),
                            DataCell(Text(vehiculo[4])),
                            DataCell(Text(vehiculo[5])),
                            DataCell(Text(vehiculo[6])),
                            DataCell(Text(vehiculo[7])),
                            DataCell(Text(vehiculo[8])),
                            DataCell(Text(vehiculo[9])),
                            DataCell(Text(vehiculo[10])),
                            DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(vehiculo))),
                            DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(vehiculo))),
                        ]
                    )
                )
                self.update()
            # Si no se está editando ninguna fila, agrega una nueva fila
            # self.mytabla.rows.append(
            #     DataRow(
            #         cells=[
            #             DataCell(Text(self.field_tipovehiculo.value)),
            #             DataCell(Text(self.field_vehiculo.value)),
            #             DataCell(Text(self.field_colorvehiculo.value)),
            #             DataCell(Text(self.field_pesovehiculo.value)),
            #             DataCell(Text(self.field_numerop.value)),
            #             DataCell(Text(self.field_marca.value)),
            #             DataCell(Text(self.field_año.value)),
            #             DataCell(Text(self.field_revisiont.value)),
            #             DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE)),
            #             DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED)),
            #         ]
                
            #     )
            # )
            # self.update()
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


    def on_item_selected_TipoVehiculo(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_tipovehiculo.value = e.control.text
        self.selected_Vehiculo_id = self.trabajador_id_map[e.control.text]
        print(self.selected_Vehiculo_id)
        self.update()

    def on_item_selected_TipoCombustible(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_vehiculo.value = e.control.text
        self.selected_trabajador_id = self.tipoCombustible_id_map[e.control.text]
        print(self.selected_trabajador_id)
        self.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaFaenas())


    ft.app(main)