import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import TrabajadorService
from Controllers.TrabajoVehiculoController import TrabajoVehiculoController
from Controllers.FaenaController import FaenaController
from Controllers.VehiculoController import VehiculoController
from Model.Entities.TrabajoVehiculo import TrabajoVehiculo
import flet as ft

# the vista de trabajadores
class TabContentVistaTrabajoVehiculo(ft.UserControl):

    #inicializa la vista
    def __init__(self):
        super().__init__()

        self.fila_editar = None
        self.selected_faena_id = None
        self.selected_vehiculo_id = None
        #text field nombre
        self.field_faena = ft.TextField(
            label="Faena",
            #hint_text="Ingrese usuario",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.faena_id_map = {}
        data = FaenaController().ListFaena()
        self.items_Faena = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[8], checked=False, on_click=self.on_item_selected_Faena) for d in data])
        for d in data:
            self.faena_id_map[d[8]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))

         #text field vehiculo
        self.field_vehiculo = ft.TextField(
            label="Vehiculo",
            #hint_text="Ingrese usuario",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.vehiculo_id_map = {}
        data = VehiculoController().ListVehiculo()
        self.items_Vehiculo = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[6], checked=False, on_click=self.on_item_selected_Vehiculo) for d in data])
        for d in data:
            self.vehiculo_id_map[d[6]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))
         #text field Nombre
        self.field_nombreT = ft.TextField(
            label="NOmbre Trabajo",
            #hint_text="Ingrese usuario",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )
         #text field Nombre
        self.field_Tipo = ft.TextField(
            label="Tipo",
            #hint_text="Ingrese usuario",
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
                ft.DataColumn(ft.Text("Faena")),
                ft.DataColumn(ft.Text("Vehiculo")),
                ft.DataColumn(ft.Text("Nombre Trabajo")),
                ft.DataColumn(ft.Text("Tipo Trabajo")),
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

    #contruye
    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_faena,self.items_Faena,self.field_vehiculo,self.items_Vehiculo],
                ),
                ft.Row(
                    [self.field_nombreT,self.field_Tipo],
                ) 
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
            spacing=20
        )
    
    #Cargado de datos para la edicion
    def cargarDatos(self, e: ft.ControlEvent, t:TrabajoVehiculo):
        self.fila_editar            = t.idTrabajosVehiculo
        self.selected_faena_id      = t.idFaenaFK
        self.selected_vehiculo_id   = t.idVehiculoFK
        self.field_faena.value       = t.faenaDescripcion
        self.field_vehiculo.value   = t.VehNumeroPlaca
        self.field_nombreT.value   = t.tvNombreTrabajo
        self.field_Tipo.value  = t.tvTipo
        self.boton_guardar.visible  = False
        self.boton_editar.visible   = True
        self.update()
        
    #DELETE
    def eliminarDatos(self, e: ft.ControlEvent, trabajador):
        controlador = TrabajoVehiculoController()
        controlador.DeleteTrabajoVechiculo(trabajador)
        # Actualiza la página para reflejar los cambios
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_faena.value       =""
        self.field_vehiculo.value   = ""
        self.field_nombreT.value   = ""
        self.field_Tipo.value  = ""
        self.update()
        print("Limpia")
        
    
    # CONTROLADo SAVE and UPDATE
    def CapturaDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        if self.fila_editar is not None:
            controlador = TrabajoVehiculoController()
            t = TrabajoVehiculo( self.fila_editar,
                            1, 
                            self.selected_faena_id, 
                            self.selected_vehiculo_id, 
                            self.field_nombreT.value, 
                            self.field_Tipo.value, 
                            )
            #EDIT
            controlador.SaveOrUpdateTrabajoVechiculo(False, t)
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            controlador = TrabajoVehiculoController()
            t = TrabajoVehiculo( self.fila_editar,
                            1, 
                            self.selected_faena_id, 
                            self.selected_vehiculo_id, 
                            self.field_nombreT.value, 
                            self.field_Tipo.value, 
                            )
            controlador.SaveOrUpdateTrabajoVechiculo(True, t)   
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

    def onFillData(self):
        #Cargas datos en la tabla
        controlador = TrabajoVehiculoController()
        #Cargas datos en la tabla
        for t in controlador.ListTrabajoVechiculos():
            def cargaEditar(t):
                return lambda e: self.cargarDatos(e, t)
            def eliminar(t):
                return lambda e: self.eliminarDatos(e, t)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(t.faenaDescripcion)),
                        DataCell(Text(t.VehNumeroPlaca)),
                        DataCell(Text(t.tvNombreTrabajo)),
                        DataCell(Text(t.tvTipo)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(t))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(t))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla
    def on_item_selected_Faena(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_faena.value = e.control.text
        self.selected_faena_id = self.faena_id_map[e.control.text]
        print(self.selected_faena_id)
        self.update()
    def on_item_selected_Vehiculo(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_vehiculo.value = e.control.text
        self.selected_vehiculo_id = self.vehiculo_id_map[e.control.text]
        print(self.selected_vehiculo_id)
        self.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaTrabajoVehiculo())
    ft.app(main)