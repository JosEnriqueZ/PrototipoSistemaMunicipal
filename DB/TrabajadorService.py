def todos_trabajadores(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Trabajador where trabActivo = 1"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_trabajador(cnxn, trabActivo, trabNombre, trabApellido, trabFechaNac, trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Trabajador (trabActivo, trabNombre, trabApellido, trabFechaNac,trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir) VALUES (?, ?, ?, ? , ?, ?, ?, ?, ?)"
    data = (trabActivo, trabNombre, trabApellido, trabFechaNac, trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Trabajador(cnxn, idTrabajador):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Trabajador WHERE idTrabajador = ?"
    data = (idTrabajador,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Trabajador(cnxn, trabActivo, trabNombre, trabApellido, trabFechaNac, trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir, idTrabajador):
    cursor = cnxn.cursor()
    update_query = "UPDATE Trabajador SET trabActivo = ? ,trabNombre = ? ,trabApellido = ? ,trabFechaNac = ? ,trabCel = ? ,trabTrabador = ? ,trabDNI = ? ,trabDireccion = ? ,trabLicenciaConducir = ? WHERE idTrabajador = ?"
    data = ( trabActivo, trabNombre, trabApellido, trabFechaNac, trabCel, trabTrabador, trabDNI, trabDireccion, trabLicenciaConducir, idTrabajador)
    
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_trabajador(cnxn, idTrabajador):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Trabajador SET trabActivo = 0 WHERE idTrabajador = ?"
    data = (idTrabajador)
    cursor.execute(delete_query, data)
    cnxn.commit()