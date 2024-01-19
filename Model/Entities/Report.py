class Report:
    def __init__(self, idReport, reportActivo, idTrabajadorFK, idFaenaFK, reportTipo, reportPlacaMaquinaria, reportFecha):
        self.idReport = idReport
        self.reportActivo = reportActivo
        self.idTrabajadorFK = idTrabajadorFK
        self.idFaenaFK = idFaenaFK
        self.reportTipo = reportTipo
        self.reportPlacaMaquinaria = reportPlacaMaquinaria
        self.reportFecha = reportFecha
    
    def get_idReport(self):
        return self.idReport

    def set_idReport(self, idReport):
        self.idReport = idReport

    def get_reportActivo(self):
        return self.reportActivo

    def set_reportActivo(self, reportActivo):
        self.reportActivo = reportActivo

    def get_idTrabajadorFK(self):
        return self.idTrabajadorFK

    def set_idTrabajadorFK(self, idTrabajadorFK):
        self.idTrabajadorFK = idTrabajadorFK

    def get_idFaenaFK(self):
        return self.idFaenaFK

    def set_idFaenaFK(self, idFaenaFK):
        self.idFaenaFK = idFaenaFK

    def get_reportTipo(self):
        return self.reportTipo

    def set_reportTipo(self, reportTipo):
        self.reportTipo = reportTipo

    def get_reportPlacaMaquinaria(self):
        return self.reportPlacaMaquinaria

    def set_reportPlacaMaquinaria(self, reportPlacaMaquinaria):
        self.reportPlacaMaquinaria = reportPlacaMaquinaria

    def get_reportFecha(self):
        return self.reportFecha

    def set_reportFecha(self, reportFecha):
        self.reportFecha = reportFecha

    def __str__(self):
        return f"Report(idReport={self.idReport}, reportActivo={self.reportActivo}, idTrabajadorFK={self.idTrabajadorFK}, idFaenaFK={self.idFaenaFK}, reportTipo={self.reportTipo}, reportPlacaMaquinaria={self.reportPlacaMaquinaria}, reportFecha={self.reportFecha})"
