class TipoVehiculo:
    def __init__(self, idTipoVehiculo, tvActivo, tvNombre, tvDescripcion):
        self.idTipoVehiculo = idTipoVehiculo
        self.tvActivo = tvActivo
        self.tvNombre = tvNombre
        self.tvDescripcion = tvDescripcion

    def __init__(self, idTipoVehiculo):
        self.idTipoVehiculo = idTipoVehiculo

    def __repr__(self):
        return f"TipoVehiculo(idTipoVehiculo={self.idTipoVehiculo}, tvActivo={self.tvActivo}, tvNombre='{self.tvNombre}', tvDescripcion='{self.tvDescripcion}')"
    
    def get_idTipoVehiculo(self):
        return self.idTipoVehiculo

    def set_idTipoVehiculo(self, idTipoVehiculo):
        self.idTipoVehiculo = idTipoVehiculo

    def get_tvActivo(self):
        return self.tvActivo

    def set_tvActivo(self, tvActivo):
        self.tvActivo = tvActivo

    def get_tvNombre(self):
        return self.tvNombre

    def set_tvNombre(self, tvNombre):
        self.tvNombre = tvNombre

    def get_tvDescripcion(self):
        return self.tvDescripcion

    def set_tvDescripcion(self, tvDescripcion):
        self.tvDescripcion = tvDescripcion
