import flet as ft
from DB import conexion
from Model.Services import UsuarioService
from Model.Entities import Usuario

class UsuarioController():


    def ListUsuario(self):
        conx = conexion.conectar()
        List = UsuarioService.todos_Usuario(conx)
        conexion.cerrar_conexion(conx)
        return List

    def DeleteTrabajadores(self, t:Usuario):
        conx = conexion.conectar()
        UsuarioService.eliminar_registro_Usuario(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateTrabajadores(self, save, t:Usuario):
        conx = conexion.conectar()
        sms  = ""
        if save:
            UsuarioService.crear_registro_Usuario(conx,t)
            sms = "Registro Guardado"
        else:
            UsuarioService.actualizar_registro_Usuario(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms