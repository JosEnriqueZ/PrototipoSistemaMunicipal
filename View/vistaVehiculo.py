import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import VehiculoService
from Model.Services import TipoVehiculoService
from Model.Services import TipoCombustibleService
from Controllers.VehiculoController import VehiculoController
from Controllers.TipoCombustibleController import TipoCombustibleController
from Model.Entities.Vehiculo import Vehiculo

import flet as ft


# the content of the icon tab
class TabContentVistaVehiculo(ft.UserControl):

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
        controlador = VehiculoController()
        data = controlador.ListTipoVehiculo()
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
        controlador = VehiculoController()
        data = controlador.ListTipoCombustible()
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
            label="Peso del Vehiculo(Toneladas)",
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
        #Cargas datos en la tabla
        self.mytabla = self.onFillData()
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

    def cargarDatos(self, e: ft.ControlEvent, v:Vehiculo):
        self.f_idvehiculo               = v.idVehiculo
        self.selected_tipoVehiculo_id   = v.tipoVehiculoFK
        self.selected_tipoCombustible_id= v.tipoCombustibleFK
        self.fila_editar                = v.idVehiculo
        self.field_tipovehiculo.value   = v[12]
        self.field_tipocombustible.value= v[13]
        # fecha_str = vehiculo[4].strftime("%d-%m-%Y")
        self.field_colorvehiculo.value  = v.VehColor
        self.field_pesovehiculo.value   = v.VehPeso
        self.field_numerop.value        = v.VehNumeroPlaca
        self.field_marca.value          = v.VehMarca
        self.field_año.value            = v.VahAnio
        self.field_revisiont.value      = v.VehRevisionTecnica
        self.field_descripcion.value    = v.VehDescripcion
        self.field_galones.value        = v.VehGalonesHoraCombustible
        self.boton_guardar.visible      = False
        self.boton_editar.visible       = True
        self.update()

    def eliminarDatos(self, e: ft.ControlEvent, vehiculo):
        controlador = VehiculoController()
        controlador.DeleteVehiculo(vehiculo)
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
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
            controlador = VehiculoController()
            v = Vehiculo(self.f_idvehiculo,
                        1, 
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
            )     
            controlador.SaveOrUpdateVehiculo(False, v)    
            self.mytabla.rows.clear()
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            """Guardar"""
            #fecha = datetime.strptime(self.field_colorvehiculo.value, "%d-%m-%Y")
            controlador = VehiculoController()
            v = Vehiculo(self.f_idvehiculo,
                        1, 
                        self.selected_tipoVehiculo_id, 
                        self.selected_tipoCombustible_id,
                        self.field_colorvehiculo.value, 
                        self.field_pesovehiculo.value, 
                        self.field_numerop.value, 
                        self.field_marca.value, 
                        self.field_año.value, 
                        self.field_revisiont.value,
                        self.field_descripcion.value,
                        self.field_galones.value)
            controlador.SaveOrUpdateVehiculo(True, v)   
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.LimpiarDatos(e)
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


    def onFillData(self):
        #Cargas datos en la tabla
        controlador = VehiculoController()
        #Cargas datos en la tabla
        for v in controlador.ListVehiculo():
            def cargaEditar(v):
                return lambda e: self.cargarDatos(e, v)
            def eliminar(v):
                return lambda e: self.eliminarDatos(e, v)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(v[12])),
                        DataCell(Text(v[13])),
                        DataCell(Text(v.VehColor)),
                        DataCell(Text(v.VehPeso)),
                        DataCell(Text(v.VehNumeroPlaca)),
                        DataCell(Text(v.VehMarca)),
                        DataCell(Text(v.VahAnio)),
                        DataCell(Text(v.VehRevisionTecnica)),
                        DataCell(Text(v.VehDescripcion)),
                        DataCell(Text(v.VehGalonesHoraCombustible)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(v))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(v))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaVehiculo())


    ft.app(main)