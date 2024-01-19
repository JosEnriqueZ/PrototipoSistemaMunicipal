from Model.Entities.Producto import Producto

def todos_Producto(cnxn):
    cursor = cnxn.cursor()
    select_query = """select p.idProducto,u.idUsuario,u.usuName,p.ProdTipo,p.ProdNombre,p.ProdFechaIngreso,p.ProdFechaUso,p.ProdStock from Producto p
inner join Usuario u on p.idUsuarioFK= u.idUsuario where p.ProdActivo=1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Producto(cnxn, p: Producto):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Producto (ProdActivo,idUsuarioFK, ProdTipo, ProdNombre,ProdFechaIngreso, ProdFechaUso, ProdStock) VALUES (?, ?, ?, ? , ?, ?, ?)"
    data = (p.ProdActivo,p.idUsuarioFK, p.ProdTipo, p.ProdNombre,p.ProdFechaIngreso, p.ProdFechaUso, p.ProdStock)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Producto(cnxn, p: Producto):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Producto WHERE idProducto = ?"
    data = (p.idProducto,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Producto(cnxn,p: Producto):
    cursor = cnxn.cursor()
    update_query = "UPDATE Producto SET ProdActivo = ? ,idUsuarioFK=? ,ProdTipo=? ,ProdNombre = ? ,ProdFechaIngreso = ? ,ProdFechaUso = ? ,ProdStock = ? WHERE idProducto = ?"
    data = ( p.ProdActivo,p.idUsuarioFK, p.ProdTipo, p.ProdNombre,p.ProdFechaIngreso, p.ProdFechaUso, p.ProdStock,p.idProducto)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Producto(cnxn, p: Producto):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Producto SET ProdActivo = 0 WHERE idProducto = ?"
    data = (p.idProducto)
    cursor.execute(delete_query, data)
    cnxn.commit()