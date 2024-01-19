from datetime import datetime

class Faena:
    def __init__(self, idFaena, faenaActivo, idTrabajadorFK, idUsuarioFK, idVehiculoFK, faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo, faenaKilometrosAreaTrabajo):
        self.idFaena = idFaena
        self.faenaActivo = faenaActivo
        self.idTrabajadorFK = idTrabajadorFK
        self.idUsuarioFK = idUsuarioFK
        self.idVehiculoFK = idVehiculoFK
        #Formateo de la fecha de Nacimiento
        fecha = datetime.strptime(faenaFechaTrabajo, "%d-%m-%Y")
        self.faenaFechaTrabajo = fecha
        self.faenaHoras = faenaHoras
        self.faenaRegion = faenaRegion
        self.faenaDescripcion = faenaDescripcion
        self.faenaDireccionTrabajo = faenaDireccionTrabajo
        self.faenaKilometrosAreaTrabajo = faenaKilometrosAreaTrabajo


    def __repr__(self):
        return f"Faena(idFaena={self.idFaena}, faenaActivo={self.faenaActivo}, idTrabajadorFK={self.idTrabajadorFK}, idUsuarioFK={self.idUsuarioFK}, idVehiculoFK={self.idVehiculoFK}, faenaFechaTrabajo={self.faenaFechaTrabajo}, faenaHoras={self.faenaHoras}, faenaRegion={self.faenaRegion}, faenaDescripcion={self.faenaDescripcion}, faenaDireccionTrabajo={self.faenaDireccionTrabajo}, faenaKilometrosAreaTrabajo={self.faenaKilometrosAreaTrabajo})"
       
    # Getter methods
    def get_idFaena(self):
        return self.idFaena

    def get_faenaActivo(self):
        return self.faenaActivo

    def get_idTrabajadorFK(self):
        return self.idTrabajadorFK

    def get_idUsuarioFK(self):
        return self.idUsuarioFK

    def get_idVehiculoFK(self):
        return self.idVehiculoFK

    def get_faenaFechaTrabajo(self):
        return self.faenaFechaTrabajo

    def get_faenaHoras(self):
        return self.faenaHoras

    def get_faenaRegion(self):
        return self.faenaRegion

    def get_faenaDescripcion(self):
        return self.faenaDescripcion

    def get_faenaDireccionTrabajo(self):
        return self.faenaDireccionTrabajo

    def get_faenaKilometrosAreaTrabajo(self):
        return self.faenaKilometrosAreaTrabajo

    # Setter methods
    def set_idFaena(self, idFaena):
        self.idFaena = idFaena

    def set_faenaActivo(self, faenaActivo):
        self.faenaActivo = faenaActivo

    def set_idTrabajadorFK(self, idTrabajadorFK):
        self.idTrabajadorFK = idTrabajadorFK

    def set_idUsuarioFK(self, idUsuarioFK):
        self.idUsuarioFK = idUsuarioFK

    def set_idVehiculoFK(self, idVehiculoFK):
        self.idVehiculoFK = idVehiculoFK

    def set_faenaFechaTrabajo(self, faenaFechaTrabajo):
        self.faenaFechaTrabajo = faenaFechaTrabajo

    def set_faenaHoras(self, faenaHoras):
        self.faenaHoras = faenaHoras

    def set_faenaRegion(self, faenaRegion):
        self.faenaRegion = faenaRegion

    def set_faenaDescripcion(self, faenaDescripcion):
        self.faenaDescripcion = faenaDescripcion

    def set_faenaDireccionTrabajo(self, faenaDireccionTrabajo):
        self.faenaDireccionTrabajo = faenaDireccionTrabajo

    def set_faenaKilometrosAreaTrabajo(self, faenaKilometrosAreaTrabajo):
        self.faenaKilometrosAreaTrabajo = faenaKilometrosAreaTrabajo
