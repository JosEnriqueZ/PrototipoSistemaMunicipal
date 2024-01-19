from Model.Entities import TrabajoVehiculo

def todos_TrabajoVehiculo(cnxn):
    cursor = cnxn.cursor()
    select_query = """select tv.*,f.faenaDescripcion,v.VehNumeroPlaca from TrabajoVehiculo tv
inner join Faena f on tv.idFaenaFK=f.idFaena
inner join Vehiculo v on v.idVehiculo=f.idVehiculoFK where tv.tvActivo=1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_TrabajoVehiculo(cnxn,tv:TrabajoVehiculo):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TrabajoVehiculo (tvActivo,idFaenaFK,idVehiculoFK,tvNombreTrabajo,tvTipo) VALUES (?, ?, ? ,?,?)"
    data = (tv.tvActivo,tv.idFaenaFK,tv.idVehiculoFK,tv.tvNombreTrabajo,tv.tvTipo)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TrabajoVehiculo(cnxn,tv:TrabajoVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TrabajoVehiculo WHERE idTrabajosVehiculo = ?"
    data = (tv.idTrabajosVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TrabajoVehiculo(cnxn,tv:TrabajoVehiculo):
    cursor = cnxn.cursor()
    update_query = "UPDATE TrabajoVehiculo SET idFaenaFK = ? ,idVehiculoFK = ? ,tvNombreTrabajo = ?,tvTipo = ? WHERE idTrabajosVehiculo = ?"
    data = ( tv.idFaenaFK,tv.idVehiculoFK,tv.tvNombreTrabajo,tv.tvTipo, tv.idTrabajosVehiculo)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TrabajoVehiculo(cnxn,tv:TrabajoVehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TrabajoVehiculo SET tcActivo = 0 WHERE idTrabajosVehiculo = ?"
    data = (tv.idTrabajosVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()