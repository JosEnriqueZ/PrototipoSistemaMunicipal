import flet as ft
from DB import conexion
from Model.Services import ReportService
from Model.Entities import Report

class ReporteController():


    def ListReporte(self):
        conx = conexion.conectar()
        ListReporte = ReportService.todos_Report(conx)
        conexion.cerrar_conexion(conx)
        return ListReporte

    def DeleteReporte(self, t:Report):
        conx = conexion.conectar()
        ReportService.eliminar_registro_Report(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateReporte(self, save, t:Report):
        conx = conexion.conectar()
        sms  = ""
        if save:
            ReportService.crear_registro_Report(conx,t)
            sms = "Registro Guardado"
        else:
            ReportService.actualizar_registro_Report(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    

        