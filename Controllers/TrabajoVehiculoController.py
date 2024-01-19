import flet as ft
from DB import conexion
from Model.Services import TrabajoVehiculoService
from Model.Entities import TrabajoVehiculo

class TrabajoVehiculoController():


    def ListTrabajoVechiculos(self):
        conx = conexion.conectar()
        List = TrabajoVehiculoService.todos_TrabajoVehiculo(conx)
        conexion.cerrar_conexion(conx)
        return List

    def DeleteTrabajoVechiculo(self, t:TrabajoVehiculo):
        conx = conexion.conectar()
        TrabajoVehiculoService.eliminar_registro_TrabajoVehiculo(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateTrabajoVechiculo(self, save, t:TrabajoVehiculo):
        conx = conexion.conectar()
        sms  = ""
        if save:
            TrabajoVehiculoService.crear_registro_TrabajoVehiculo(conx,t)
            sms = "Registro Guardado"
        else:
            TrabajoVehiculoService.actualizar_registro_TrabajoVehiculo(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms