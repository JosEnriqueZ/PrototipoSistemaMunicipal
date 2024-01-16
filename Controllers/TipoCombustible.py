class TipoCombustible:
    def __init__(self, idTipoCombustible, tcActivo, tcCodigoCombustible, tcNombre):
        self.idTipoCombustible = idTipoCombustible
        self.tcActivo = tcActivo
        self.tcCodigoCombustible = tcCodigoCombustible
        self.tcNombre = tcNombre

    def __repr__(self):
        return f"TipoCombustible(idTipoCombustible={self.idTipoCombustible}, tcActivo={self.tcActivo}, tcCodigoCombustible='{self.tcCodigoCombustible}', tcNombre='{self.tcNombre}')"
    # Getter y Setter para idTipoCombustible
    def get_idTipoCombustible(self):
        return self.idTipoCombustible

    def set_idTipoCombustible(self, idTipoCombustible):
        self.idTipoCombustible = idTipoCombustible

    # Getter y Setter para tcActivo
    def get_tcActivo(self):
        return self.tcActivo

    def set_tcActivo(self, tcActivo):
        self.tcActivo = tcActivo

    # Getter y Setter para tcCodigoCombustible
    def get_tcCodigoCombustible(self):
        return self.tcCodigoCombustible

    def set_tcCodigoCombustible(self, tcCodigoCombustible):
        self.tcCodigoCombustible = tcCodigoCombustible

    # Getter y Setter para tcNombre
    def get_tcNombre(self):
        return self.tcNombre

    def set_tcNombre(self, tcNombre):
        self.tcNombre = tcNombre
