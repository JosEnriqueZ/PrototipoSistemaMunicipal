import flet as ft
from DB import conexion
from Model.Services import TrabajadorService
from Model.Entities import Trabajador

class TrabajadorController():


    def ListTrabajadores(self):
        conx = conexion.conectar()
        ListTrabajadores = TrabajadorService.todos_trabajadores(conx)
        conexion.cerrar_conexion(conx)
        return ListTrabajadores

    def DeleteTrabajadores(self, t:Trabajador):
        conx = conexion.conectar()
        TrabajadorService.eliminar_registro_trabajador(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateTrabajadores(self, save, t:Trabajador):
        conx = conexion.conectar()
        sms  = ""
        if save:
            TrabajadorService.crear_registro_trabajador(conx,t)
            sms = "Registro Guardado"
        else:
            TrabajadorService.actualizar_registro_Trabajador(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    

        


