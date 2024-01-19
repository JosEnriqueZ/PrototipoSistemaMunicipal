import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import ProductoService
from Controllers.ProductoController import ProductoController
from Controllers.UsuarioController import UsuarioController
from Model.Entities.Producto import Producto
from Model.Entities.Usuario import Usuario
import flet as ft

# the vista de Producto
class TabContentVistaProducto(ft.UserControl):

    #inicializa la vista
    def __init__(self):
        super().__init__()
        self.fila_editar = None
        self.selected_usuario_id = None
        #text field nombre
        self.field_name = ft.TextField(
            label="Usuario",
            hint_text="Ingrese usuario",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.usuario_id_map = {}
        data = UsuarioController().ListUsuario()
        self.items_Usuario = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[3], checked=False, on_click=self.on_item_selected_USuario) for d in data])
        for d in data:
            self.usuario_id_map[d[3]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))
            
        # text field descripcion
        self.field_nombre = ft.TextField(
            label="Nombre",
            hint_text="Ingrese nombre producto",
            value="",
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,
        )
         # text field descripcion
        self.field_TIpoproducto = ft.TextField(
            label="Tipo producto",
            hint_text="Ingrese tipo producto",
            value="",
            #helper_text="Optional[str]",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # text field Fecha
        self.field_fechaIngreso = ft.TextField(
            label="Fecha Ingreso",
            hint_text="DD-MM-YYYY",
            value="",
            on_change=self.validar_fecha,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # text field Fecha
        self.field_fechaUso = ft.TextField(
            label="Fecha Uso",
            hint_text="DD-MM-YYYY",
            value="",
            on_change=self.validar_fecha,
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text field Numero de stock
        self.field_stock = ft.TextField(
            label="stock",
            hint_text="Ingrese numero stock",
            value="",
            on_change=self.validar_numeros,
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
                ft.DataColumn(ft.Text("Usuario")),
                ft.DataColumn(ft.Text("Tipo producto")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Fecha Ingreso")),
                ft.DataColumn(ft.Text("Fecha Uso")),
                ft.DataColumn(ft.Text("Stock")),
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
                    [self.field_name,self.items_Usuario,self.field_nombre],
                ) ,
                ft.Row(
                    [self.field_TIpoproducto,self.field_fechaIngreso],
                ) ,
                ft.Row(
                    [self.field_fechaUso,self.field_stock],
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
    def cargarDatos(self, e: ft.ControlEvent, tv:Producto):
        self.selected_usuario_id = tv.idUsuario
        self.fila_editar                = tv.idProducto
        self.field_name.value           = tv.usuName
        self.field_TIpoproducto.value    = tv.ProdTipo
        self.field_nombre.value    = tv.ProdNombre
        self.field_fechaIngreso.value    = tv.ProdFechaIngreso.strftime("%d-%m-%Y")
        self.field_fechaUso.value    = tv.ProdFechaUso.strftime("%d-%m-%Y")
        self.field_stock.value    = tv.ProdStock
        self.boton_guardar.visible      = False
        self.boton_editar.visible       = True
        self.update()
        
    #DELETE
    def eliminarDatos(self, e: ft.ControlEvent, tv:Producto):
        controlador = ProductoController()
        controlador.DeleteProducto(tv)
        # Actualiza la página para reflejar los cambios
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_name.value           = ""
        self.field_TIpoproducto.value    = ""
        self.field_nombre.value    = ""
        self.field_fechaIngreso.value    = ""
        self.field_fechaUso.value    = ""
        self.field_stock.value    = ""
        self.update()
        print("Limpia")
        
    
    # CONTROLADo SAVE and UPDATE
    def CapturaDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        if self.fila_editar is not None:
            controlador = ProductoController()
            t = Producto( self.fila_editar,
                            1, 
                            self.selected_usuario_id,
                            self.field_TIpoproducto.value, 
                            self.field_nombre.value,
                            self.field_fechaIngreso.value ,  
                            self.field_fechaUso.value ,   
                            self.field_stock.value 
                            )
            #EDIT
            controlador.SaveOrUpdateProducto(False, t)
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            controlador = ProductoController()
            t = Producto( self.fila_editar,
                            1, 
                            self.selected_usuario_id,
                            self.field_TIpoproducto.value, 
                            self.field_nombre.value,
                            self.field_fechaIngreso.value ,  
                            self.field_fechaUso.value ,   
                            self.field_stock.value 
                            )
            controlador.SaveOrUpdateProducto(True, t)   
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
        controlador = ProductoController()
        #Cargas datos en la tabla
        for p in controlador.ListProducto():
            def cargaEditar(p):
                return lambda e: self.cargarDatos(e, p)
            def eliminar(p):
                return lambda e: self.eliminarDatos(e, p)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(p.usuName)),
                        DataCell(Text(p.ProdTipo)),
                        DataCell(Text(p.ProdNombre)),
                        DataCell(Text(p.ProdFechaIngreso)),
                        DataCell(Text(p.ProdFechaUso)),
                        DataCell(Text(p.ProdStock)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(p))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(p))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla
    
    
    def on_item_selected_USuario(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_name.value = e.control.text
        self.selected_usuario_id = self.usuario_id_map[e.control.text]
        print(self.selected_usuario_id)
        self.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaProducto())
    ft.app(main)