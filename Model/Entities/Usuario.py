class Usuario:
    def __init__(self, idUsuario, usuActivo, idTrabajadorFK, usuName, usuRut, usuPass, usuRol):
        self.idUsuario = idUsuario
        self.usuActivo = usuActivo
        self.idTrabajadorFK = idTrabajadorFK
        self.usuName = usuName
        self.usuRut = usuRut
        self.usuPass = usuPass
        self.usuRol = usuRol

    def get_idUsuario(self):
        return self.idUsuario

    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def get_usuActivo(self):
        return self.usuActivo

    def set_usuActivo(self, usuActivo):
        self.usuActivo = usuActivo

    def get_idTrabajadorFK(self):
        return self.idTrabajadorFK

    def set_idTrabajadorFK(self, idTrabajadorFK):
        self.idTrabajadorFK = idTrabajadorFK

    def get_usuName(self):
        return self.usuName

    def set_usuName(self, usuName):
        self.usuName = usuName

    def get_usuRut(self):
        return self.usuRut

    def set_usuRut(self, usuRut):
        self.usuRut = usuRut

    def get_usuPass(self):
        return self.usuPass

    def set_usuPass(self, usuPass):
        self.usuPass = usuPass

    def get_usuRol(self):
        return self.usuRol

    def set_usuRol(self, usuRol):
        self.usuRol = usuRol

    def __repr__(self):
        return f"Usuario(idUsuario={self.idUsuario}, usuActivo={self.usuActivo}, idTrabajadorFK={self.idTrabajadorFK}, usuName={self.usuName}, usuRut={self.usuRut}, usuPass={self.usuPass}, usuRol={self.usuRol})"
    