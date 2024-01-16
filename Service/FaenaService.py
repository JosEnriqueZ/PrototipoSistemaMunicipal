def todos_faenas(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Faena"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Faena(cnxn, faenaActivo, idTrabajadorFK, idUsuarioFK, idVehiculoFK, faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Faena (faenaActivo,idTrabajadorFK, idUsuarioFK, idVehiculoFK,faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo) VALUES (?, ?, ?, ? , ?, ?, ?, ?, ?, ?)"
    data = (faenaActivo, idTrabajadorFK, idUsuarioFK, idVehiculoFK, faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Faena(cnxn, idTrabajador):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Faena WHERE idFaena = ?"
    data = (idTrabajador,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Faena(cnxn, faenaActivo, idTrabajadorFK, idUsuarioFK, idVehiculoFK, faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo, idFaena):
    cursor = cnxn.cursor()
    update_query = "UPDATE Faena SET faenaActivo = ? ,idTrabajadorFK = ? ,idUsuarioFK = ? ,idVehiculoFK = ? ,faenaFechaTrabajo = ? ,faenaHoras = ? ,faenaRegion = ? ,faenaDescripcion = ? ,faenaDireccionTrabajo = ? ,faenaKilometrosAreaTrabajo = ? WHERE idFaena = ?"
    data = ( faenaActivo, idTrabajadorFK, idUsuarioFK, idVehiculoFK, faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo, idFaena)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Faena(cnxn, idFaena):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Faena SET faenaActivo = 0 WHERE idFaena = ?"
    data = (idFaena)
    cursor.execute(delete_query, data)
    cnxn.commit()