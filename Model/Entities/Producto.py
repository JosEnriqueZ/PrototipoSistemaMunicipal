from datetime import datetime
class Producto:
    def __init__(self, idProducto, ProdActivo, idUsuarioFK, ProdTipo, ProdNombre, fechaingreso, ProdFechaUso, ProdStock):
        self.idProducto = idProducto
        self.ProdActivo = ProdActivo
        self.idUsuarioFK = idUsuarioFK
        self.ProdTipo = ProdTipo
        self.ProdNombre = ProdNombre
        #Formateo de la fecha de Nacimiento
        fecha1 = datetime.strptime(fechaingreso, "%d-%m-%Y")
        self.fechaingreso = fecha1
        fecha2 = datetime.strptime(ProdFechaUso, "%d-%m-%Y")
        self.ProdFechaIngreso = fecha2
        self.ProdFechaUso = ProdFechaUso
        self.ProdStock = ProdStock
    def get_idProducto(self):
        return self.idProducto

    def set_idProducto(self, idProducto):
        self.idProducto = idProducto

    def get_ProdActivo(self):
        return self.ProdActivo

    def set_ProdActivo(self, ProdActivo):
        self.ProdActivo = ProdActivo

    def get_idUsuarioFK(self):
        return self.idUsuarioFK

    def set_idUsuarioFK(self, idUsuarioFK):
        self.idUsuarioFK = idUsuarioFK

    def get_ProdTipo(self):
        return self.ProdTipo

    def set_ProdTipo(self, ProdTipo):
        self.ProdTipo = ProdTipo

    def get_ProdNombre(self):
        return self.ProdNombre

    def set_ProdNombre(self, ProdNombre):
        self.ProdNombre = ProdNombre

    def get_ProdFechaIngreso(self):
        return self.ProdFechaIngreso

    def set_ProdFechaIngreso(self, ProdFechaIngreso):
        self.ProdFechaIngreso = ProdFechaIngreso

    def get_ProdFechaUso(self):
        return self.ProdFechaUso

    def set_ProdFechaUso(self, ProdFechaUso):
        self.ProdFechaUso = ProdFechaUso

    def get_ProdStock(self):
        return self.ProdStock

    def set_ProdStock(self, ProdStock):
        self.ProdStock = ProdStock

    def __str__(self):
        return f"Producto(idProducto={self.idProducto}, ProdActivo={self.ProdActivo}, idUsuarioFK={self.idUsuarioFK}, ProdTipo={self.ProdTipo}, ProdNombre={self.ProdNombre}, ProdFechaIngreso={self.ProdFechaIngreso}, ProdFechaUso={self.ProdFechaUso}, ProdStock={self.ProdStock})"
