from datetime import datetime

class Trabajador:

    def __init__(self, idTrabajador, trabActivo, trabNombre, trabApellido, trabfechaNac, trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir):
        self.idTrabajador = idTrabajador
        self.trabActivo = trabActivo
        self.trabNombre = trabNombre
        self.trabApellido = trabApellido
        #Formateo de la fecha de Nacimiento
        fecha = datetime.strptime(trabfechaNac, "%d-%m-%Y")
        self.trabfechaNac = fecha
        self.trabCel = trabCel
        self.trabTrabador = trabTrabador
        self.trabDNI = trabDNI
        self.trabDireccion = trabDireccion
        self.trabLicenciaConducir = trabLicenciaConducir

    def __str__(self):
        return f"MiEntidad(idTrabajador={self.idTrabajador}, trabNombre={self.trabNombre})"

    def get_idTrabajador(self):
        return self.idTrabajador

    def set_idTrabajador(self, idTrabajador):
        self.idTrabajador = idTrabajador

    def get_trabActivo(self):
        return self.trabActivo

    def set_trabActivo(self, trabActivo):
        self.trabActivo = trabActivo

    def get_trabNombre(self):
        return self.trabNombre

    def set_trabNombre(self, trabNombre):
        self.trabNombre = trabNombre

    def get_trabApellido(self):
        return self.trabApellido

    def set_trabApellido(self, trabApellido):
        self.trabApellido = trabApellido

    def get_trabfechaNac(self):
        return self.trabfechaNac

    def set_trabfechaNac(self, trabfechaNac):
        self.trabfechaNac = trabfechaNac

    def get_trabCel(self):
        return self.trabCel

    def set_trabCel(self, trabCel):
        self.trabCel = trabCel

    def get_trabTrabador(self):
        return self.trabTrabador

    def set_trabTrabador(self, trabTrabador):
        self.trabTrabador = trabTrabador

    def get_trabDNI(self):
        return self.trabDNI

    def set_trabDNI(self, trabDNI):
        self.trabDNI = trabDNI

    def get_trabDireccion(self):
        return self.trabDireccion

    def set_trabDireccion(self, trabDireccion):
        self.trabDireccion = trabDireccion

    def get_trabLicenciaConducir(self):
        return self.trabLicenciaConducir

    def set_trabLicenciaConducir(self, trabLicenciaConducir):
        self.trabLicenciaConducir = trabLicenciaConducir
