import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import TipoCombustibleService
from Controllers.TipoCombustibleController import TipoCombustibleController
from Model.Entities.TipoCombustible import TipoCombustible
import flet as ft

# the vista de TipoCOmbustible
class TabContentVistaTipoCombustible(ft.UserControl):

    #inicializa la vista
    def __init__(self):
        super().__init__()
        
        self.fila_editar = None
        #text field nombre
        self.field_nombreCombustible = ft.TextField(
            label="Nombre Combustible",
            hint_text="Ingrese Tipo de Combustible",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text field apellido
        self.field_codigoCombustible = ft.TextField(
            label="Codigo Combustible",
            hint_text="Ingrese Codigo de Combustible",
            value="",
            on_change=self.validar_numeros,
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.NUMBER,
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
                ft.DataColumn(ft.Text("Codigo Combustible")),
                ft.DataColumn(ft.Text("Nombre Combustible")),
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
                    [self.field_nombreCombustible,self.field_codigoCombustible],
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
            spacing=20
        )
    
    #Cargado de datos para la edicion
    def cargarDatos(self, e: ft.ControlEvent, t:TipoCombustible):
        self.fila_editar            = t.idTipoCombustible
        self.field_nombreCombustible.value       = t.tcNombre
        self.field_codigoCombustible.value   = t.tcCodigoCombustible
        self.boton_guardar.visible  = False
        self.boton_editar.visible   = True
        self.update()
        
    #DELETE
    def eliminarDatos(self, e: ft.ControlEvent, tipocombustible):
        controlador = TipoCombustibleController()
        controlador.DeleteTipoCombustible(tipocombustible)
        # Actualiza la página para reflejar los cambios
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_nombreCombustible.value =""
        self.field_codigoCombustible.value = ""
        self.update()
        print("Limpia")
        
    
    # CONTROLADo SAVE and UPDATE
    def CapturaDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        if self.fila_editar is not None:
            controlador = TipoCombustibleController()
            t = TipoCombustible( self.fila_editar,
                            1, 
                            self.field_nombreCombustible.value, 
                            self.field_codigoCombustible.value, 
                            )
            #EDIT
            controlador.SaveOrUpdateTipoCombustible(False, t)
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            controlador = TipoCombustibleController()
            t = TipoCombustible( self.fila_editar,
                            1, 
                            self.field_nombreCombustible.value, 
                            self.field_codigoCombustible.value, 
                            )
            controlador.SaveOrUpdateTipoCombustible(True, t)   
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
        controlador = TipoCombustibleController()
        #Cargas datos en la tabla
        for t in controlador.ListTipoCombustible():
            def cargaEditar(t):
                return lambda e: self.cargarDatos(e, t)
            def eliminar(t):
                return lambda e: self.eliminarDatos(e, t)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(t.tcCodigoCombustible)),
                        DataCell(Text(t.tcNombre)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(t))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(t))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaTipoCombustible())
    ft.app(main)