def todos_Producto(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Producto"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Producto(cnxn, ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Producto (ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock) VALUES (?, ?, ?, ? , ?, ?, ?)"
    data = (ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Producto(cnxn, idProducto):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Producto WHERE idProducto = ?"
    data = (idProducto,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Producto(cnxn,ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock, idProducto):
    cursor = cnxn.cursor()
    update_query = "UPDATE Producto SET ProdActivo = ? ,idTrabajadorFK = ? ,idUsuarioFK = ? ,idVehiculoFK = ? ,faenaFechaTrabajo = ? ,faenaHoras = ? ,faenaRegion = ? ,faenaDescripcion = ? ,faenaDireccionTrabajo = ? ,faenaKilometrosAreaTrabajo = ? WHERE idProducto = ?"
    data = ( ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock, idProducto)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Producto(cnxn, idProducto):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Producto SET ProdActivo = 0 WHERE idProducto = ?"
    data = (idProducto)
    cursor.execute(delete_query, data)
    cnxn.commit()