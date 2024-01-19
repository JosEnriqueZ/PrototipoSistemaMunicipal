import math
from flet import *
from datetime import datetime
from DB import conexion
from Model.Services import ReportService
from Controllers.ReportController import ReporteController
from Model.Entities.Report import Report
import flet as ft

# the vista de TipoCOmbustible
class TabContentVistaReporte(ft.UserControl):

    #inicializa la vista
    def __init__(self):
        super().__init__()

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
        self.mytabla.rows.clear()
        #Cargas datos en la tabla
        self.mytabla = self.onFillData()
        return ft.Column(
            [
                ft.Text("Reporte:", weight=ft.FontWeight.BOLD, size=20),
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
    
    def onFillData(self):
        #Cargas datos en la tabla
        controlador = ReporteController()
        #Cargas datos en la tabla
        for t in controlador.ListReporte():
            def cargaEditar(t):
                return lambda e: self.cargarDatos(e, t)
            def eliminar(t):
                return lambda e: self.eliminarDatos(e, t)
            self.mytabla.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(t.idTrabajadorFK)),
                        DataCell(Text(t.idFaenaFK)),
                        DataCell(Text(t.reportTipo)),
                        DataCell(Text(t.reportPlacaMaquinaria)),
                        DataCell(Text(t.reportFecha)),
                    ]
                )
            )
        print('Tabla Refresh')
        return self.mytabla


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentVistaReporte())
    ft.app(main)