import math
from flet import *
from datetime import datetime
from DB import conexion
from Service import VehiculoService
from Service import TipoVehiculoService
from Service import TipoCombustibleService

import flet as ft


# the content of the icon tab
class TabContentVistaMaquinaria(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.f_idvehiculo = None
        self.fila_editar = None
        self.selected_tipoCombustible_id = None
        self.selected_tipoVehiculo_id = None
        
        #text field Vehiculo
        self.field_tipovehiculo = ft.TextField(
            label="Tipo Vehiculo",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.tipoVehiculo_id_map = {}
        data = TipoVehiculoService.todos_TipoVehiculo(conexion.conectar())
        self.items_TipoVehiculo = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[2], checked=False, on_click=self.on_item_selected_TipoVehiculo) for d in data])
        for d in data:
            self.tipoVehiculo_id_map[d[2]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))

        # text field COmbustible
        self.field_tipocombustible = ft.TextField(
            label="Tipo Combustible",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        self.tipoCombustible_id_map = {}
        data = TipoCombustibleService.todos_TipoCombustible(conexion.conectar())
        self.items_TipoCombustible = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[3], checked=False, on_click=self.on_item_selected_TipoCombustible) for d in data])
        for d in data:
            self.tipoCombustible_id_map[d[3]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoCombustible.items.append(ft.PopupMenuItem(text=d[2]))

        # text Color del Vehiculo
        self.field_colorvehiculo = ft.TextField(
            label="Color del Vehiculo",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Peso del Vehiculo
        self.field_pesovehiculo = ft.TextField(
            label="Peso del Vehiculo",
            hint_text="Ingrese Peso del Vehiculo",
            value="",
            on_change=self.validar_numeros,
            keyboard_type=ft.KeyboardType.NUMBER,

        )

        # text field Numero de Placa
        self.field_numerop = ft.TextField(
            label="Numero de Placa",
            hint_text="Ingrese Numero de Placa",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Marca
        self.field_marca = ft.TextField(
            label="Marca",
            hint_text="Ingrese la Marca",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )

        # text field Fabricacion
        self.field_año = ft.TextField(
            label="Año de Fabricacion",
            hint_text="Ingrese el Año de Fabricacion",
            value="",
            keyboard_type=ft.KeyboardType.NUMBER,
        
        )

        # text field Revision Tecnica
        self.field_revisiont = ft.TextField(
            label="Revision Tecnica",
            hint_text="Revision Tecnica",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field Descripcion
        self.field_descripcion = ft.TextField(
            label="Descripcion",
            hint_text="Ingrese su categoria de licencia de conducir",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        # text field Galones x hora Combustible
        self.field_galones = ft.TextField(
            label="Galones x hora Combustible",
            hint_text="Galones x hora Combustible",
            value="",
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
                ft.DataColumn(ft.Text("T Vehiculo")),
                ft.DataColumn(ft.Text("Ti Combustible")),
                ft.DataColumn(ft.Text("Color")),
                ft.DataColumn(ft.Text("Peso")),
                ft.DataColumn(ft.Text("Placa")),
                ft.DataColumn(ft.Text("Marca")),
                ft.DataColumn(ft.Text("Año")),
                ft.DataColumn(ft.Text("Revision Tecnica")),
                ft.DataColumn(ft.Text("Descripcion")),
                ft.DataColumn(ft.Text("GalxHora")),
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
                    [self.field_tipovehiculo,self.items_TipoVehiculo,self.field_tipocombustible,self.items_TipoCombustible],
                ),
                ft.Row(
                    [self.field_colorvehiculo,self.field_pesovehiculo],
                ),
                ft.Row(
                    [self.field_numerop, self.field_marca],
                ),
                ft.Row(
                    [self.field_año, self.field_revisiont],
                ),
                ft.Row(
                    [self.field_descripcion, self.field_galones],
                ),
                
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=11
        )
        self.mytabla.rows.clear()
        vehiculos = VehiculoService.todos_Vehiculo(conexion.conectar())
        
        for vehiculo in vehiculos:
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
                        DataCell(Text(vehiculo[11])),
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
        self.selected_tipoVehiculo_id = vehiculo[1]
        self.selected_tipoCombustible_id = vehiculo[2]
        self.fila_editar = vehiculo[0]
        self.field_tipovehiculo.value = vehiculo[12]
        self.field_tipocombustible.value = vehiculo[13]
        # fecha_str = vehiculo[4].strftime("%d-%m-%Y")
        self.field_colorvehiculo.value = vehiculo[4]
        self.field_pesovehiculo.value = vehiculo[5]
        self.field_numerop.value = vehiculo[6]
        self.field_marca.value = vehiculo[7]
        self.field_año.value = vehiculo[8]
        self.field_revisiont.value = vehiculo[9]
        self.field_descripcion.value = vehiculo[10]
        self.field_galones.value = vehiculo[11]
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
        self.field_tipocombustible.value = ""
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
            self.mytabla.rows[self.fila_editar-1].cells[1].content.value = self.field_tipocombustible.value
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
                                                        self.selected_tipoVehiculo_id, 
                                                        self.selected_tipoCombustible_id,
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
            vehiculos = VehiculoService.todos_Vehiculo(conexion.conectar())
            for vehiculo in vehiculos:
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
                            DataCell(Text(vehiculo[11])),
                            DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(vehiculo))),
                            DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(vehiculo))),
                        ]
                    )
                )
                # self.update()
            vehiculos = VehiculoService.todos_Vehiculo(conexion.conectar())
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
            self.update()
        else:

            """Guardar"""
            #fecha = datetime.strptime(self.field_colorvehiculo.value, "%d-%m-%Y")
            VehiculoService.crear_registro_Vehiculo(conexion.conectar(), 1, self.selected_tipoVehiculo_id, 
                                                    self.selected_tipoCombustible_id,
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
            vehiculos = VehiculoService.todos_Vehiculo(conexion.conectar())
            for vehiculo in vehiculos:
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
                            DataCell(Text(vehiculo[11])),
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
            #             DataCell(Text(self.field_tipocombustible.value)),
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

    # def validar_fecha(self, e: ft.ControlEvent):
    #     # Verifica si el valor ingresado por el usuario es una fecha válida.
    #     fecha_str = e.control.value.strip()
    #     try:
    #         # Intenta convertir la cadena de texto a una fecha.
    #         datetime.strptime(fecha_str, "%d-%m-%Y")
    #         e.control.error_text = ""
    #     except ValueError:
    #         # Si la conversión falla, muestra un mensaje de error.
    #         e.control.error_text = "Por favor, ingrese una fecha válida en el formato DD-MM-YYYY."
    #     self.update()


    def on_item_selected_TipoVehiculo(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_tipovehiculo.value = e.control.text
        self.selected_tipoVehiculo_id = self.tipoVehiculo_id_map[e.control.text]
        print(self.selected_tipoVehiculo_id)
        self.update()

    def on_item_selected_TipoCombustible(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_tipocombustible.value = e.control.text
        self.selected_tipoCombustible_id = self.tipoCombustible_id_map[e.control.text]
        print(self.selected_tipoCombustible_id)
        self.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaMaquinaria())


    ft.app(main)