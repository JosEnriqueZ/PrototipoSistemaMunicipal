import flet as ft
from DB import conexion
from Model.Services import ProductoService
from Model.Entities import Producto

class ProductoController():


    def ListProducto(self):
        conx = conexion.conectar()
        ListProducto = ProductoService.todos_Producto(conx)
        conexion.cerrar_conexion(conx)
        return ListProducto

    def DeleteProducto(self, t:Producto):
        conx = conexion.conectar()
        ProductoService.eliminar_registro_Producto(conx,t)
        conexion.cerrar_conexion(conx)
        return True
    
    def SaveOrUpdateProducto(self, save, t:Producto):
        conx = conexion.conectar()
        sms  = ""
        if save:
            ProductoService.crear_registro_Producto(conx,t)
            sms = "Registro Guardado"
        else:
            ProductoService.actualizar_registro_Producto(conx,t)
            sms = "Registro Editado"   
        conexion.cerrar_conexion(conx)
        return sms
    

        