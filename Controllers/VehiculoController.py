import flet as ft
from DB import conexion
from Model.Services import VehiculoService
from Model.Services import TipoCombustibleService
from Model.Services import TipoVehiculoService
from Model.Entities import Vehiculo

class VehiculoController():


    def ListVehiculo(self):
        conx = conexion.conectar()
        ListVehiculo = VehiculoService.todos_Vehiculo(conx)
        conexion.cerrar_conexion(conx)
        return ListVehiculo

    def DeleteVehiculo(self, v:Vehiculo):
        conx = conexion.conectar()
        VehiculoService.eliminar_registro_Vehiculo(conx,v)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateVehiculo(self, save, v:Vehiculo):
        conx = conexion.conectar()
        sms  = ""
        if save:
            VehiculoService.crear_registro_Vehiculo(conx,v)
            sms = "Registro Guardado"
        else:
            VehiculoService.actualizar_registro_Vehiculo(conx,v)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    
    def ListTipoVehiculo(self):
        conx = conexion.conectar()
        ListTipoVehiculo = TipoVehiculoService.todos_TipoVehiculo(conx)
        conexion.cerrar_conexion(conx)
        return ListTipoVehiculo
    
    def ListTipoCombustible(self):
        conx = conexion.conectar()
        ListTipoVehiculo = TipoCombustibleService.todos_TipoCombustible(conx)
        conexion.cerrar_conexion(conx)
        return ListTipoVehiculo

        


