def todos_Report(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Report"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Report(cnxn,reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Report (reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha) VALUES (?, ?, ?, ? , ?, ?)"
    data = (reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Report(cnxn, idTrabajador):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Report WHERE idReport = ?"
    data = (idTrabajador,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Report(cnxn,reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha, idReport):
    cursor = cnxn.cursor()
    update_query = "UPDATE Report SET reportActivo = ? ,idTrabajadorFK = ? ,idFaenaFK = ? ,reportTipo = ? ,reportPlacaMaquinaria = ? ,reportFecha = ? WHERE idReport = ?"
    data = ( reportActivo,idTrabajadorFK,idFaenaFK,reportTipo,reportPlacaMaquinaria,reportFecha, idReport)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Report(cnxn, idReport):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Report SET reportActivo = 0 WHERE idReport = ?"
    data = (idReport)
    cursor.execute(delete_query, data)
    cnxn.commit()