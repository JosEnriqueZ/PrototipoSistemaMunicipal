class Vehiculo:
    def __init__(self, idVehiculo, VehActivo, tipoVehiculoFK, tipoCombustibleFK, VehColor, VehPeso, VehNumeroPlaca, VehMarca, VahAnio, VehRevisionTecnica, VehDescripcion, VehGalonesHoraCombustible):
        self.idVehiculo = idVehiculo
        self.VehActivo = VehActivo
        self.tipoVehiculoFK = tipoVehiculoFK
        self.tipoCombustibleFK = tipoCombustibleFK
        self.VehColor = VehColor
        self.VehPeso = VehPeso
        self.VehNumeroPlaca = VehNumeroPlaca
        self.VehMarca = VehMarca
        self.VahAnio = VahAnio
        self.VehRevisionTecnica = VehRevisionTecnica
        self.VehDescripcion = VehDescripcion
        self.VehGalonesHoraCombustible = VehGalonesHoraCombustible

    def get_idVehiculo(self):
        return self.idVehiculo

    def set_idVehiculo(self, idVehiculo):
        self.idVehiculo = idVehiculo

    def get_VehActivo(self):
        return self.VehActivo

    def set_VehActivo(self, VehActivo):
        self.VehActivo = VehActivo

    def get_tipoVehiculoFK(self):
        return self.tipoVehiculoFK

    def set_tipoVehiculoFK(self, tipoVehiculoFK):
        self.tipoVehiculoFK = tipoVehiculoFK

    def get_tipoCombustibleFK(self):
        return self.tipoCombustibleFK

    def set_tipoCombustibleFK(self, tipoCombustibleFK):
        self.tipoCombustibleFK = tipoCombustibleFK

    def get_VehColor(self):
        return self.VehColor

    def set_VehColor(self, VehColor):
        self.VehColor = VehColor

    def get_VehPeso(self):
        return self.VehPeso

    def set_VehPeso(self, VehPeso):
        self.VehPeso = VehPeso

    def get_VehNumeroPlaca(self):
        return self.VehNumeroPlaca

    def set_VehNumeroPlaca(self, VehNumeroPlaca):
        self.VehNumeroPlaca = VehNumeroPlaca

    def get_VehMarca(self):
        return self.VehMarca

    def set_VehMarca(self, VehMarca):
        self.VehMarca = VehMarca

    def get_VahAnio(self):
        return self.VahAnio

    def set_VahAnio(self, VahAnio):
        self.VahAnio = VahAnio

    def get_VehRevisionTecnica(self):
        return self.VehRevisionTecnica

    def set_VehRevisionTecnica(self, VehRevisionTecnica):
        self.VehRevisionTecnica = VehRevisionTecnica

    def get_VehDescripcion(self):
        return self.VehDescripcion

    def set_VehDescripcion(self, VehDescripcion):
        self.VehDescripcion = VehDescripcion

    def get_VehGalonesHoraCombustible(self):
        return self.VehGalonesHoraCombustible

    def set_VehGalonesHoraCombustible(self, VehGalonesHoraCombustible):
        self.VehGalonesHoraCombustible = VehGalonesHoraCombustible


    def __repr__(self):
        return f"Vehiculo(idVehiculo={self.idVehiculo}, VehActivo={self.VehActivo}, tipoVehiculoFK={self.tipoVehiculoFK}, tipoCombustibleFK={self.tipoCombustibleFK}, VehColor='{self.VehColor}', VehPeso={self.VehPeso}, VehNumeroPlaca='{self.VehNumeroPlaca}', VehMarca='{self.VehMarca}', VahAnio={self.VahAnio}, VehRevisionTecnica='{self.VehRevisionTecnica}', VehDescripcion='{self.VehDescripcion}', VehGalonesHoraCombustible={self.VehGalonesHoraCombustible})"