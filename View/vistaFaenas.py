import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import FaenaService
from Model.Services import TrabajadorService
from Model.Services import UsuarioService
from Model.Services import VehiculoService
from Controllers.FaenaController import FaenaController
from Controllers.VehiculoController import VehiculoController
from Controllers.FaenaController import FaenaController
from Model.Entities.Faena import Faena

import flet as ft
# the content of the icon tab
class TabContentVistaFaenas(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.f_idfaena = None
        self.fila_editar = None
        self.selected_trabajador_id = None
        self.selected_usuario_id = None
        self.selected_Vehiculo_id = None
        
        #text field Trabajador
        self.field_trabajador = ft.TextField(
            label="Trabajadores",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.trabajador_id_map = {}
        controlador = FaenaController()
        data = controlador.ListTrabajadores()
        self.items_Trabajador = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[2], checked=False, on_click=self.on_item_selected_Trabajador) for d in data])
        for d in data:
            self.trabajador_id_map[d[2]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_Trabajador.items.append(ft.PopupMenuItem(text=d[2]))

        # text field usuario
        self.field_usuario = ft.TextField(
            label="Usuarios",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.usuario_id_map = {}
        controlador = FaenaController()
        data = controlador.ListUsuario()
        self.items_Usuario = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[3], checked=False, on_click=self.on_item_selected_Usuario) for d in data])
        for d in data:
            self.usuario_id_map[d[3]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_Trabajador.items.append(ft.PopupMenuItem(text=d[2]))

        # text field Vehiculo
        self.field_vehiculo = ft.TextField(
            label="Vehiculos",
            value="",
            on_change=self.validar_nombre,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,

        )
        self.vehiculo_id_map = {}
        controlador = VehiculoController()
        data = controlador.ListVehiculo()
        self.items_Vehiculo = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[6], checked=False, on_click=self.on_item_selected_Vehiculo) for d in data])
        for d in data:
            self.vehiculo_id_map[d[6]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
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
            label="Kilometros",
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
                ft.DataColumn(ft.Text("Usuario")),
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
                    [self.field_trabajador,self.items_Trabajador,self.field_usuario,self.items_Usuario],
                ),
                ft.Row(
                    [self.field_vehiculo,self.items_Vehiculo,self.field_fecha,self.field_horas],
                ),
                ft.Row(
                    [self.field_region, self.field_descripcion,self.field_kilometrosa],
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
            #scroll=ft.ScrollMode.HIDDEN,
            spacing=20
        )

    def cargarDatos(self,e: ft.ControlEvent,f:Faena):
        self.fila_editar            = f.idFaena
        self.f_idfaena              = f.idFaena
        self.selected_trabajador_id = f.idTrabajadorFK
        self.field_trabajador.value = f[11]
        self.selected_usuario_id    = f.idUsuarioFK
        self.field_usuario.value    = f[12]
        self.selected_Vehiculo_id   = f.idVehiculoFK
        self.field_vehiculo.value   = f[13]
        #self.field_fecha.value = faena[5]
        fecha_str                   = f.faenaFechaTrabajo.strftime("%d-%m-%Y")
        self.field_fecha.value = fecha_str
        self.field_horas.value = f.faenaHoras
        self.field_region.value = f.faenaRegion
        self.field_descripcion.value = f.faenaDescripcion
        self.field_direccion.value = f.faenaDireccionTrabajo
        self.field_kilometrosa.value = f.faenaKilometrosAreaTrabajo
        # fecha_str = faena[4].strftime("%d-%m-%Y")
        self.boton_guardar.visible=False
        self.boton_editar.visible=True
        self.update()

    def eliminarDatos(self, e: ft.ControlEvent, Faena):
        controlador = FaenaController()
        controlador.DeleteFaena(Faena)
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.f_idfaena =""
        self.field_trabajador.value = ""
        self.field_usuario.value = ""
        self.field_vehiculo.value = ""
        self.field_fecha.value =""
        self.field_horas.value = ""
        self.field_region.value = ""
        self.field_descripcion.value = ""
        self.field_direccion.value = ""
        self.field_kilometrosa.value = ""
        self.update()
    
    
    def EditaryGuardar(self, e: ft.ControlEvent):

        """Editar"""
        self.boton_guardar.visible=True
        self.boton_editar.visible=False

        if self.fila_editar is not None:
            controlador = FaenaController()
            v = Faena(self.f_idfaena,
                        1, 
                        self.selected_trabajador_id,
                        self.selected_usuario_id,
                        self.selected_Vehiculo_id,
                        self.field_fecha.value, 
                        self.field_horas.value, 
                        self.field_region.value, 
                        self.field_descripcion.value,    
                        self.field_direccion.value,  
                        self.field_kilometrosa.value,     
            )     
            controlador.SaveOrUpdateFaena(False, v)    
            self.mytabla.rows.clear()
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            """Guardar"""
            controlador = FaenaController()
            v = Faena(self.f_idfaena,
                        1, 
                        self.selected_trabajador_id,
                        self.selected_usuario_id,
                        self.selected_Vehiculo_id,
                        self.field_fecha.value, 
                        self.field_horas.value, 
                        self.field_region.value, 
                        self.field_descripcion.value,    
                        self.field_direccion.value,  
                        self.field_kilometrosa.value,     
            )   
            controlador.SaveOrUpdateFaena(True, v)   
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

    #llena la listas
    #lista de trabajadores
    def on_item_selected_Trabajador(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_trabajador.value = e.control.text
        self.selected_trabajador_id = self.trabajador_id_map[e.control.text]
        print(self.selected_trabajador_id)
        self.update()

    def on_item_selected_Usuario(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_usuario.value = e.control.text
        self.selected_usuario_id = self.usuario_id_map[e.control.text]
        print(self.selected_usuario_id)
        self.update()

    #lista de vehiculos
    def on_item_selected_Vehiculo(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_vehiculo.value = e.control.text
        self.selected_Vehiculo_id = self.vehiculo_id_map[e.control.text]
        print(self.selected_Vehiculo_id)
        self.update()

    def onFillData(self):
        #Cargas datos en la tabla
        controlador = FaenaController()
        #Cargas datos en la tabla
        for u in controlador.ListFaena():
            def cargaEditar(v):
                return lambda e: self.cargarDatos(e, u)
            def eliminar(v):
                return lambda e: self.eliminarDatos(e, u)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(u[11])),
                        DataCell(Text(u[12])),
                        DataCell(Text(u[13])),
                        DataCell(Text(u.faenaFechaTrabajo)),
                        DataCell(Text(u.faenaHoras)),
                        DataCell(Text(u.faenaRegion)),
                        DataCell(Text(u.faenaDescripcion)),
                        DataCell(Text(u.faenaDireccionTrabajo)),
                        DataCell(Text(u.faenaKilometrosAreaTrabajo)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(u))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(u))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaFaenas())


    ft.app(main)