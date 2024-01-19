from Model.Entities import Report

def todos_Report(cnxn):
    cursor = cnxn.cursor()
    select_query = """SELECT r.idReport,r.reportActivo,(t.trabNombre+' '+ t.trabApellido) as Nombre,
                        f.faenaDescripcion,r.reportTipo,r.reportPlacaMaquinaria,r.reportFecha FROM Report r
                        inner join Trabajador t on  r.idTrabajadorFK=t.idTrabajador
                        inner join Faena f on f.idTrabajadorFK=t.idTrabajador"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Report(cnxn,re:Report):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Report (reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha) VALUES (?, ?, ?, ? , ?, ?)"
    data = (re.reportActivo,re.idTrabajadorFK,re.idFaenaFK,re.reportTipo,re.reportPlacaMaquinaria,re.reportFecha)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Report(cnxn, re:Report):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Report WHERE idReport = ?"
    data = (re.idTrabajador,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Report(cnxn,re:Report):
    cursor = cnxn.cursor()
    update_query = "UPDATE Report SET reportActivo = ? ,idTrabajadorFK = ? ,idFaenaFK = ? ,reportTipo = ? ,reportPlacaMaquinaria = ? ,reportFecha = ? WHERE idReport = ?"
    data = ( re.reportActivo,re.idTrabajadorFK,re.idFaenaFK,re.reportTipo,re.reportPlacaMaquinaria,re.reportFecha, re.idReport)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Report(cnxn, re:Report):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Report SET reportActivo = 0 WHERE idReport = ?"
    data = (re.idReport)
    cursor.execute(delete_query, data)
    cnxn.commit()