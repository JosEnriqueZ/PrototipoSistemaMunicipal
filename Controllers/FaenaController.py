import flet as ft
from DB import conexion
from Model.Services import FaenaService
from Model.Entities import Faena

class FaenaController():


    def ListFaena(self):
        conx = conexion.conectar()
        ListProducto = FaenaService.todos_faenas(conx)
        conexion.cerrar_conexion(conx)
        return ListProducto

    def DeleteFaena(self, t:Faena):
        conx = conexion.conectar()
        FaenaService.eliminar_registro_Faena(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateFaena(self, save, t:Faena):
        conx = conexion.conectar()
        sms  = ""
        if save:
            FaenaService.crear_registro_Faena(conx,t)
            sms = "Registro Guardado"
        else:
            FaenaService.actualizar_registro_Faena(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    
