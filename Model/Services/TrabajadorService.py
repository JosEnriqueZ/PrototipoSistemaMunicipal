
from Model.Entities import Trabajador
from datetime import datetime

def todos_trabajadores(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Trabajador where trabActivo = 1"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_trabajador(cnxn, t:Trabajador):
    cursor = cnxn.cursor()
    insert_query =  """INSERT INTO Trabajador 
                    (trabActivo, trabNombre, trabApellido, 
                    trabfechaNac,trabCel, trabTrabador, trabDNI, 
                    trabDireccion, trabLicenciaConducir) 
                    VALUES (?, ?, ?, ? , ?, ?, ?, ?, ?)"""
    data = (t.trabActivo, t.trabNombre, t.trabApellido, t.trabfechaNac, t.trabCel, t.trabTrabador, t.trabDNI, t.trabDireccion, t.trabLicenciaConducir)
    cursor.execute(insert_query, data)
    print('trabajador Creado')
    cnxn.commit()

def leer_registro_Trabajador(cnxn, t:Trabajador):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Trabajador WHERE idTrabajador = ?"
    data = (t.idTrabajador)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Trabajador(cnxn, t:Trabajador):
    cursor = cnxn.cursor()
    update_query =  """UPDATE Trabajador SET 
                    trabActivo      = ?,
                    trabNombre      = ?,
                    trabApellido    = ?,
                    trabFechaNac    = ?,
                    trabCel         = ?,
                    trabTrabador    = ?,
                    trabDNI         = ?,    
                    trabDireccion   = ?,
                    trabLicenciaConducir = ? 
                    WHERE idTrabajador = ?"""
    data = ( t.trabActivo, t.trabNombre, t.trabApellido, t.trabfechaNac, t.trabCel, t.trabTrabador, t.trabDNI, t.trabDireccion, t.trabLicenciaConducir, t.idTrabajador)
    cursor.execute(update_query, data)
    print('trabajador Actualizado')
    cnxn.commit()

def eliminar_registro_trabajador(cnxn, t:Trabajador):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Trabajador SET trabActivo = 0 WHERE idTrabajador = ?"
    data = (t.idTrabajador)
    cursor.execute(delete_query, data)
    print(f"trabajador Eliminado: idTrabajador={t.idTrabajador}, trabNombre={t.trabNombre})")
    cnxn.commit()


