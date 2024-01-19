import flet as ft
from DB import conexion
from Model.Services import TipoVehiculoService
from Model.Entities import TipoVehiculo

class TipoVehiculoController():


    def ListTipoVehiculo(self):
        conx = conexion.conectar()
        ListTipoVehiculo = TipoVehiculoService.todos_TipoVehiculo(conx)
        conexion.cerrar_conexion(conx)
        return ListTipoVehiculo

    def DeleteTipoVehiculo(self, tv:TipoVehiculo):
        conx = conexion.conectar()
        TipoVehiculoService.eliminar_registro_TipoVehiculo(conx,v)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateTipoVehiculo(self, save, tv:TipoVehiculo):
        conx = conexion.conectar()
        sms  = ""
        if save:
            TipoVehiculoService.crear_registro_TipoVehiculo(conx,tv)
            sms = "Registro Guardado"
        else:
            TipoVehiculoService.actualizar_registro_TipoVehiculo(conx,tv)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    

        


