class TrabajoVehiculo:
    def __init__(self, idTrabajosVehiculo, tvActivo, idFaenaFK, idVehiculoFK, tvNombreTrabajo, tvTipo):
        self.idTrabajosVehiculo = idTrabajosVehiculo
        self.tvActivo = tvActivo
        self.idFaenaFK = idFaenaFK
        self.idVehiculoFK = idVehiculoFK
        self.tvNombreTrabajo = tvNombreTrabajo
        self.tvTipo = tvTipo
    
    
    def get_idTrabajosVehiculo(self):
        return self.idTrabajosVehiculo

    def set_idTrabajosVehiculo(self, idTrabajosVehiculo):
        self.idTrabajosVehiculo = idTrabajosVehiculo

    def get_tvActivo(self):
        return self.tvActivo

    def set_tvActivo(self, tvActivo):
        self.tvActivo = tvActivo

    def get_idFaenaFK(self):
        return self.idFaenaFK

    def set_idFaenaFK(self, idFaenaFK):
        self.idFaenaFK = idFaenaFK

    def get_idVehiculoFK(self):
        return self.idVehiculoFK

    def set_idVehiculoFK(self, idVehiculoFK):
        self.idVehiculoFK = idVehiculoFK

    def get_tvNombreTrabajo(self):
        return self.tvNombreTrabajo

    def set_tvNombreTrabajo(self, tvNombreTrabajo):
        self.tvNombreTrabajo = tvNombreTrabajo

    def get_tvTipo(self):
        return self.tvTipo

    def set_tvTipo(self, tvTipo):
        self.tvTipo = tvTipo
