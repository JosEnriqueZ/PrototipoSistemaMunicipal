import flet as ft
from DB import conexion
from Model.Services import FaenaService
from Model.Services import TrabajadorService
from Model.Services import VehiculoService
from Model.Services import UsuarioService
from Model.Entities import Faena
from Model.Entities import Vehiculo

class FaenaController():


    def ListFaena(self):
        conx = conexion.conectar()
        ListFaena = FaenaService.todos_faenas(conx)
        conexion.cerrar_conexion(conx)
        return ListFaena

    def DeleteFaena(self, v:Faena):
        conx = conexion.conectar()
        FaenaService.eliminar_registro_Faena(conx,v)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateFaena(self, save, v:Faena):
        conx = conexion.conectar()
        sms  = ""
        if save:
            FaenaService.crear_registro_Faena(conx,v)
            sms = "Registro Guardado"
        else:
            FaenaService.actualizar_registro_Faena(conx,v)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    
    def ListTrabajadores(self):
        conx = conexion.conectar()
        ListTrabajadores = TrabajadorService.todos_trabajadores(conx)
        conexion.cerrar_conexion(conx)
        return ListTrabajadores
    
    def ListUsuario(self):
        conx = conexion.conectar()
        ListUsuario = UsuarioService.todos_Usuario(conx)
        conexion.cerrar_conexion(conx)
        return ListUsuario
    
    def ListVehiculo(self):
        conx = conexion.conectar()
        ListTipoFaena = VehiculoService.todos_Vehiculo(conx)
        conexion.cerrar_conexion(conx)
        return ListTipoFaena

    def ListByFechaFaena(self, fecha):
        conx = conexion.conectar()
        ListTipoFaena = FaenaService.leer_registro_FaenaxFecha(conx,fecha)
        conexion.cerrar_conexion(conx)
        return ListTipoFaena
    
    def ListByVehiculoId(self, idvehiculo):
        conx = conexion.conectar()
        ListTipoFaena =FaenaService.leer_registro_FaenaxVehiculo(conx,idvehiculo)
        conexion.cerrar_conexion(conx)
        return ListTipoFaena
        
    def ListAllReporte(self):
        conx = conexion.conectar()
        ListFaena = FaenaService.leer_registro_FaenaTotalReporte(conx)
        conexion.cerrar_conexion(conx)
        return ListFaena


