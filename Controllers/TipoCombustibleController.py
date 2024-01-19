import flet as ft
from DB import conexion
from Model.Services import TipoCombustibleService
from Model.Entities import TipoCombustible

class TipoCombustibleController():


    def ListTipoCombustible(self):
        conx = conexion.conectar()
        ListTrabajadores = TipoCombustibleService.todos_TipoCombustible(conx)
        conexion.cerrar_conexion(conx)
        return ListTrabajadores

    def DeleteTipoCombustible(self, t:TipoCombustible):
        conx = conexion.conectar()
        TipoCombustibleService.eliminar_registro_TipoCombustible(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateTipoCombustible(self, save, t:TipoCombustible):
        conx = conexion.conectar()
        sms  = ""
        if save:
            TipoCombustibleService.crear_registro_TipoCombustible(conx,t)
            sms = "Registro Guardado"
        else:
            TipoCombustibleService.actualizar_registro_TipoCombustible(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    

        
