import flet as ft
from random import choice
from DB import conexion
from DB import FaenaService
from DB import ProductoService
from DB import ReportService
from DB import TipoCombustibleService
from DB import TipoVehiculoService
from DB import TrabajadorService
from DB import TrabajoVehiculoService
from DB import UsuarioService
from DB import VehiculoService

#pruebas
#Faena-ojo
def probandoseleccionFaena():
    FaenaService.todos_faenas(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarFaena():
    FaenaService.crear_registro_Faena(conexion.conectar(), 1, 1, 1, 1, "02-05-2021","12","Arequipa","Arequipa","Arequipa","10")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarFaena()
#Productos-
def probandoseleccionProductos():
    ProductoService.todos_Producto(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarProductos():
    ProductoService.crear_registro_Producto(conexion.conectar(), 1, 1, "prueba", "prueba", "02-05-2021", "02-05-2021", "1")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarProductos()
#Report-
def probandoseleccionReport():
    ReportService.todos_Report(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarReport():
    ReportService.crear_registro_Report(conexion.conectar(),1,1,1,"report tipo 1","Placa","02-05-2021")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarReport()
#TipoCombustible-
def probandoseleccionTipoCombustible():
    TipoCombustibleService.todos_TipoCombustible(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarTipoCombustible():
    TipoCombustibleService.crear_registro_TipoCombustible(conexion.conectar(),1,10,"Petroleo")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarTipoCombustible()

#TipoVehiculo-
def probandoseleccionTipoVehiculo():
    TipoVehiculoService.todos_TipoVehiculo(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarTipoVehiculo():
    TipoVehiculoService.crear_registro_TipoVehiculo(conexion.conectar(),1,"Retroescavadora","Retroescavadora")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarTipoVehiculo()
    
#Trabajadores-
def probandoseleccionTrabajador():
    datosTrabajador= TrabajadorService.todos_trabajadores(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
    return datosTrabajador
def probandoAgregarTrabajador():
    TrabajadorService.crear_registro_trabajador(conexion.conectar(), 1, "Juan", "Perez", "1990-01-01", "9999", "1", "99999", "Ave", "999")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarTrabajador()
#probandoseleccionTrabajador()
    
#TrabajoVehiculo-ojo
def probandoseleccionTrabajoVehiculo():
    TrabajoVehiculoService.todos_TrabajoVehiculo(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarTrabajoVehiculo():
    TrabajoVehiculoService.crear_registro_TrabajoVehiculo(conexion.conectar(),1,1,1,"Ejemplo1","Tipo 1")
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarTrabajoVehiculo()
#Usuario-
def probandoSeleccionUsuario():
    UsuarioService.todos_Usuario(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoagregarUsuario():
    UsuarioService.crear_registro_Usuario(conexion.conectar(), 1, 1, "admin", "12345", "12345", "admin")
    conexion.cerrar_conexion(conexion.conectar())
#probandoagregarUsuario() 
#Vehiculo-
def probandoseleccionVehiculo():
    VehiculoService.todos_Vehiculo(conexion.conectar())
    conexion.cerrar_conexion(conexion.conectar())
def probandoAgregarVehiculo():
    VehiculoService.crear_registro_Vehiculo(conexion.conectar(),1,2,1,"Amarillo",2500.22,"Vasda2","Marca2","2020-05-02","Revision2","Descripcion2",12)
    conexion.cerrar_conexion(conexion.conectar())
#probandoAgregarVehiculo()