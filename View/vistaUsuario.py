import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import UsuarioService
from Controllers.UsuarioController import UsuarioController
from Controllers.TipoCombustibleController import TipoCombustibleController
from Model.Entities.Usuario import Usuario

import flet as ft


# the content of the icon tab
class TabContentVistaUsuario(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.f_idUsuario = None
        self.fila_editar = None
        self.selected_Trabajador_id = None
        
        #text field Trabajador
        self.field_Trabajador = ft.TextField(
            label="Trabajdor",
            value="",
            on_change=self.validar_nombre,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.trabajadorid_map = {}
        controlador = UsuarioController()
        data = controlador.ListTrabajadores()
        self.items_Trabajador = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[2], checked=False, on_click=self.on_item_selected_Trabajador) for d in data])
        for d in data:
            self.trabajadorid_map[d[2]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoUsuario.items.append(ft.PopupMenuItem(text=d[2]))

        # text NAME
        self.field_name = ft.TextField(
            label="Name Usuario",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text RUT
        self.field_rut = ft.TextField(
            label="RUT Usuario",
            hint_text="Ingrese RUT del Usuario",
            value="",
            on_change=self.validar_numeros,
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        # text field PASS
        self.field_pass = ft.TextField(
            label="PASSWORD",
            hint_text="Ingrese una password",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )

        # text field ROL
        self.field_rol = ft.TextField(
            label="ROL",
            hint_text="Ingrese el Rol",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
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
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("RUT")),
                ft.DataColumn(ft.Text("Password")),
                ft.DataColumn(ft.Text("Rol")),
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
                    [self.field_Trabajador,self.items_Trabajador,self.field_rut],
                ),
                ft.Row(
                    [self.field_name,self.field_pass,self.field_rol],
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

    def cargarDatos(self, e: ft.ControlEvent, v:Usuario):
        self.f_idUsuario               = v.idUsuario
        self.selected_Trabajador_id    = v.idTrabajadorFK
        self.fila_editar               = v.idUsuario
        self.field_Trabajador.value    = v[7]
        self.field_name.value          = v.usuName
        self.field_rut.value           = v.usuRut
        self.field_pass.value          = v.usuPass
        self.field_rol.value           = v.usuRol
        self.boton_guardar.visible     = False
        self.boton_editar.visible      = True
        self.update()

    def eliminarDatos(self, e: ft.ControlEvent, Usuario):
        controlador = UsuarioController()
        controlador.DeleteUsuario(Usuario)
        self.mytabla.rows.clear()
        self.mytabla = self.onFillData()
        self.update()
    
    def LimpiarDatos(self, e: ft.ControlEvent):
        self.boton_guardar.visible=True
        self.boton_editar.visible=False
        self.field_Trabajador.value =""
        self.field_name.value = ""
        self.field_rut.value = ""
        self.field_pass.value = ""
        self.field_rol.value = ""
        self.update()
    
    
    def EditaryGuardar(self, e: ft.ControlEvent):

        """Editar"""
        self.boton_guardar.visible=True
        self.boton_editar.visible=False

        if self.fila_editar is not None:   
            controlador = UsuarioController()
            v = Usuario(self.f_idUsuario,
                        1, 
                        self.selected_Trabajador_id, 
                        self.field_name.value, 
                        self.field_rut.value, 
                        self.field_pass.value, 
                        self.field_rol.value,       
            )     
            controlador.SaveOrUpdateUsuario(False, v)    
            self.mytabla.rows.clear()
            # Actualiza las demás celdas de la misma manera
            self.fila_editar = None  # Restablece el índice de la fila que se está editando
        else:
            """Guardar"""
            #fecha = datetime.strptime(self.field_colorUsuario.value, "%d-%m-%Y")
            controlador = UsuarioController()
            v = Usuario(self.f_idUsuario,
                        1, 
                        self.selected_Trabajador_id, 
                        self.field_name.value, 
                        self.field_rut.value, 
                        self.field_pass.value, 
                        self.field_rol.value,       
            )  
            controlador.SaveOrUpdateUsuario(True, v)   
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


    def on_item_selected_Trabajador(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_Trabajador.value = e.control.text
        self.selected_Trabajador_id = self.trabajadorid_map[e.control.text]
        print(self.selected_Trabajador_id)
        self.update()

    def onFillData(self):
        #Cargas datos en la tabla
        controlador = UsuarioController()
        #Cargas datos en la tabla
        for u in controlador.ListUsuario():
            def cargaEditar(v):
                return lambda e: self.cargarDatos(e, u)
            def eliminar(v):
                return lambda e: self.eliminarDatos(e, u)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(u[7])),
                        DataCell(Text(u.usuName)),
                        DataCell(Text(u.usuRut)),
                        DataCell(Text(u.usuPass)),
                        DataCell(Text(u.usuRol)),
                        DataCell(ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,on_click=cargaEditar(u))),
                        DataCell(ft.IconButton(icon=ft.icons.DELETE,icon_color=ft.colors.RED,on_click=eliminar(u))),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla

if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaUsuario())


    ft.app(main)