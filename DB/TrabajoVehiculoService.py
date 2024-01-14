def todos_TrabajoVehiculo(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TrabajoVehiculo"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_TrabajoVehiculo(cnxn,tvActivo,idFaenaFK,idVehiculoFK,tvNombreTrabajo,tvTipo):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TrabajoVehiculo (tvActivo,idFaenaFK,idVehiculoFK,tvNombreTrabajo,tvTipo) VALUES (?, ?, ? ,?,?)"
    data = (tvActivo,idFaenaFK,idVehiculoFK,tvNombreTrabajo,tvTipo)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TrabajoVehiculo(cnxn, idTrabajosVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TrabajoVehiculo WHERE idTrabajosVehiculo = ?"
    data = (idTrabajosVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TrabajoVehiculo(cnxn,tcActivo,tcCodigoCombustible,tcNombre, idTrabajosVehiculo):
    cursor = cnxn.cursor()
    update_query = "UPDATE TrabajoVehiculo SET tcActivo = ? tcCodigoCombustible = ? tcNombre = ? WHERE idTrabajosVehiculo = ?"
    data = ( tcActivo,tcCodigoCombustible,tcNombre, idTrabajosVehiculo)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TrabajoVehiculo(cnxn, idTrabajosVehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TrabajoVehiculo SET tcActivo = 0 WHERE idTrabajosVehiculo = ?"
    data = (idTrabajosVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()