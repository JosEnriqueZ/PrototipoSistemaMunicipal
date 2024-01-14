def todos_Usuario(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Usuario"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Usuario(cnxn,usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Usuario (usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol) VALUES (?, ?, ? ,?,?,?)"
    data = (usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Usuario(cnxn, idUsuario):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Usuario WHERE idUsuario = ?"
    data = (idUsuario,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Usuario(cnxn,usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol, idUsuario):
    cursor = cnxn.cursor()
    update_query = "UPDATE Usuario SET usuActivo = ? idTrabajadorFK = ? usuName = ? usuRut = ? usuPass = ? usuRol = ? WHERE idUsuario = ?"
    data = ( usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol, idUsuario)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Usuario(cnxn, idUsuario):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Usuario SET usuActivo = 0 WHERE idUsuario = ?"
    data = (idUsuario)
    cursor.execute(delete_query, data)
    cnxn.commit()