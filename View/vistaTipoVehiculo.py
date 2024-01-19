import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import TipoVehiculoService
from Controllers.TipoVehiculoController import TipoVehiculoController
from Model.Entities.TipoVehiculo import TipoVehiculo
import flet as ft

# the vista de TipoVehiculoes
class TabContentVistaTipoVehiculo(ft.UserControl):

    #inicializa la vista
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

        # text field descripcion
        self.field_descripcion = ft.TextField(
            label="Descripcion",
            hint_text="Ingrese su Descripcion",
            value="",
            #helper_text="Optional[str]",
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
                ft.DataColumn(ft.Text("Descripcion")),
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
                    [self.field_name,self.field_descripcion],
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
    def cargarDatos(self, e: ft.ControlEvent, tv:TipoVehiculo):
        self.fila_editar                = tv.idTipoVehiculo
        self.field_name.value           = tv.tvNombre
        self.field_descripcion.value    = tv.tvDescripcion
        self.boton_guardar.visible      = False
        self.boton_editar.visible       = True
        self.update()
        
    #DELETE
    def eliminarDatos(self, e: ft.ControlEvent, TipoVehiculo):
        controlador = TipoVehiculoController()
        controlador.DeleteTipoVehiculo(TipoVehiculo)
        # Actualiza la página para reflejar los cambios
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_name.value =""
        self.field_descripcion.value = ""
        self.update()
        print("Limpia")
        
    
    # CONTROLADo SAVE and UPDATE
    def CapturaDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        if self.fila_editar is not None:
            controlador = TipoVehiculoController()
            t = TipoVehiculo( self.fila_editar,
                            1, 
                            self.field_name.value, 
                            self.field_descripcion.value
                            )
            #EDIT
            controlador.SaveOrUpdateTipoVehiculoes(False, t)
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            controlador = TipoVehiculoController()
            t = TipoVehiculo( self.fila_editar,
                            1, 
                            self.field_name.value, 
                            self.field_descripcion.value
                            )
            controlador.SaveOrUpdateTipoVehiculo(True, t)   
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

    def onFillData(self):
        #Cargas datos en la tabla
        controlador = TipoVehiculoController()
        #Cargas datos en la tabla
        for tv in controlador.ListTipoVehiculo():
            def cargaEditar(tv):
                return lambda e: self.cargarDatos(e, tv)
            def eliminar(tv):
                return lambda e: self.eliminarDatos(e, tv)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(tv.tvNombre)),
                        DataCell(Text(tv.tvDescripcion)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(tv))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(tv))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaTipoVehiculo())
    ft.app(main)