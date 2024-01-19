import flet as ft
from DB import conexion
from Model.Services import UsuarioService
from Model.Services import TrabajadorService
from Model.Entities import Usuario

class UsuarioController():


    def ListUsuario(self):
        conx = conexion.conectar()
        ListUsuario = UsuarioService.todos_Usuario(conx)
        conexion.cerrar_conexion(conx)
        return ListUsuario

    def DeleteUsuario(self, u:Usuario):
        conx = conexion.conectar()
        UsuarioService.eliminar_registro_Usuario(conx,u)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateUsuario(self, save, u:Usuario):
        conx = conexion.conectar()
        sms  = ""
        if save:
            UsuarioService.crear_registro_Usuario(conx,u)
            sms = "Registro Guardado"
        else:
            UsuarioService.actualizar_registro_Usuario(conx,u)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    
    def ListTrabajadores(self):
        conx = conexion.conectar()
        ListTrabajadores = TrabajadorService.todos_trabajadores(conx)
        conexion.cerrar_conexion(conx)
        return ListTrabajadores
    

        


