from Model.Entities.Usuario import Usuario

def todos_Usuario(cnxn):
    cursor = cnxn.cursor()
    select_query = """SELECT u.*, CONCAT(t.trabApellido,' - ',t.trabNombre)
                    FROM usuario as u 
                    JOIN Trabajador as t ON t.idTrabajador= u.idTrabajadorFK 
	                where u.usuActivo = 1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Usuario(cnxn,u:Usuario):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Usuario (usuActivo,idTrabajadorFK,usuName,usuRut,usuPass,usuRol) VALUES (?, ?, ? ,?,?,?)"
    data = (u.usuActivo,u.idTrabajadorFK,u.usuName,u.usuRut,u.usuPass,u.usuRol)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Usuario(cnxn, u:Usuario):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Usuario WHERE idUsuario = ?"
    data = (u.idUsuario,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Usuario(cnxn,u:Usuario):
    cursor = cnxn.cursor()
    update_query = "UPDATE Usuario SET usuActivo = ? ,idTrabajadorFK = ? ,usuName = ? ,usuRut = ? ,usuPass = ? ,usuRol = ? WHERE idUsuario = ?"
    data = ( u.usuActivo,u.idTrabajadorFK,u.usuName,u.usuRut,u.usuPass,u.usuRol, u.idUsuario)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Usuario(cnxn, u:Usuario):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Usuario SET usuActivo = 0 WHERE idUsuario = ?"
    data = (u.idUsuario)
    cursor.execute(delete_query, data)
    cnxn.commit()