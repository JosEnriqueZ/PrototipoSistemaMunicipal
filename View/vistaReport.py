import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import ReportService
from Controllers.ReportController import ReporteController
from Controllers.VehiculoController import VehiculoController
from Controllers.ReportController import ReporteController
from Controllers.FaenaController import FaenaController

from Model.Entities.Report import Report
import flet as ft

# the vista de TipoCOmbustible
class TabContentVistaReporte(ft.UserControl):

    #inicializa la vista
    def __init__(self):
        super().__init__()
        self.f_idvehiculo = None
        self.selected_Vehiculo_id = None
        self.selected_Fecha = None

        #text field Vehiculo--------------------------
        self.field_vehiculo = ft.TextField(
            label="Vehiculo - Placa",
            value="",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.Vehiculo_id_map = {}
        controlador = VehiculoController()
        data = controlador.ListVehiculo()
        self.items_TipoVehiculo = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[6], checked=False, on_click=self.on_item_selected_Vehiculo) for d in data])
        for d in data:
            self.Vehiculo_id_map[d[6]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))

        #text field Fecha------------------------------
        self.field_fecha = ft.TextField(
            label="Fecha Report",
            value="",
            on_change=self.validar_fecha,
            keyboard_type=ft.KeyboardType.TEXT,
        )
        self.fecha_map = {}
        controlador = FaenaController()
        data = controlador.ListFaena()
        self.items_Fecha = ft.PopupMenuButton(
            items=[ft.PopupMenuItem(text=d[5], checked=False, on_click=self.on_item_selected_Fecha) for d in data])
        for d in data:
            self.fecha_map[d[5]] = d[0]  # Suponiendo que d[0] es el ID y d[2] es el nombre
            #self.items_TipoVehiculo.items.append(ft.PopupMenuItem(text=d[2]))

        self.mytabla = ft.DataTable(
            border=ft.border.all(2, "black"),
            border_radius=10,
            width=1180,
            vertical_lines=ft.border.BorderSide(3, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            column_spacing=50,
            bgcolor="white",
            columns=[
                ft.DataColumn(ft.Text("Trabajador")),
                ft.DataColumn(ft.Text("Faena")),
                ft.DataColumn(ft.Text("Report Tipo")),
                ft.DataColumn(ft.Text("Report Placa MAquinaria")),
                ft.DataColumn(ft.Text("Report Fecha")),
            ],
            rows=[],
        )

    #contruye
    def build(self):

        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_vehiculo,
                     self.items_TipoVehiculo,
                     self.field_fecha,
                     self.items_Fecha],
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
                ft.Text("Reporte:", weight=ft.FontWeight.BOLD, size=20),
                all_fields,
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
    

    def on_item_selected_Vehiculo(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_vehiculo.value = e.control.text
        self.selected_Vehiculo_id = self.Vehiculo_id_map[e.control.text]
        print(self.selected_Vehiculo_id)
        self.update()

    def on_item_selected_Fecha(self,e: ft.ControlEvent):
        # Asigna el valor seleccionado al TextField
        self.field_fecha.value = e.control.text
        self.selected_field_fecha = self.fecha_map[e.control.text]
        self.validar_fecha(e)
        print(self.selected_field_fecha)
        self.update()

    def validar_fecha(self, e: ft.ControlEvent):
            # Verifica si el valor ingresado por el usuario contiene solo letras.
            if not e.control.value.is=='':
                print('VALUE: '+e.control.value)
                controlador = FaenaController()
                controlador.ListByFechaFaena(e.control.value)
            else:
                e.control.error_text = ""
                print('VALUE: '+e.control.value)
            self.update()

    def onFillData(self):
        #Cargas datos en la tabla
        controlador = FaenaController()
        #Cargas datos en la tabla
        for t in controlador.ListFaena():
            def cargaEditar(t):
                return lambda e: self.cargarDatos(e, t)
            def eliminar(t):
                return lambda e: self.eliminarDatos(e, t)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(t[0])),
                        DataCell(Text(t[1])),
                        DataCell(Text(t[2])),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaReporte())
    ft.app(main)