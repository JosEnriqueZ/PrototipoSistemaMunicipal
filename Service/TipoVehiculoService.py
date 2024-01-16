def todos_TipoVehiculo(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoVehiculo"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def TipoVehiculo_Nombre(cnxn, tvNombre):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoVehiculo where tvNombre = ?"
    data = (tvNombre,)
    cursor.execute(select_query,data)
    rows = cursor.fetchone()
    print(rows)
    return rows

def crear_registro_TipoVehiculo(cnxn,tvActivo,tvNombre,tvDescripcion):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TipoVehiculo (tvActivo,tvNombre,tvDescripcion) VALUES (?, ?, ?)"
    data = (tvActivo,tvNombre,tvDescripcion)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TipoVehiculo(cnxn, idTipoVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoVehiculo WHERE idTipoVehiculo = ?"
    data = (idTipoVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TipoVehiculo(cnxn,tcActivo,tcCodigoCombustible,tcNombre, idTipoCombustible):
    cursor = cnxn.cursor()
    update_query = "UPDATE TipoVehiculo SET tcActivo = ? ,tcCodigoCombustible = ? ,tcNombre = ? WHERE idTipoVehiculo = ?"
    data = ( tcActivo,tcCodigoCombustible,tcNombre, idTipoCombustible)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TipoVehiculo(cnxn, idTipoVehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TipoVehiculo SET tcActivo = 0 WHERE idTipoVehiculo = ?"
    data = (idTipoVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()