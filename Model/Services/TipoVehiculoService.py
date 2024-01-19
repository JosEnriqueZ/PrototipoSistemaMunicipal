from Model.Entities import TipoVehiculo

def todos_TipoVehiculo(cnxn):
    cursor = cnxn.cursor()
    select_query = """SELECT * FROM TipoVehiculo where tvActivo = 1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def TipoVehiculo_Nombre(cnxn, tv:TipoVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoVehiculo where tvNombre = ?"
    data = (tv.tvNombre)
    cursor.execute(select_query,data)
    rows = cursor.fetchone()
    return rows

def crear_registro_TipoVehiculo(cnxn, tv:TipoVehiculo):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TipoVehiculo (tvActivo,tvNombre,tvDescripcion) VALUES (?, ?, ?)"
    data = (tv.tvActivo,tv.tvNombre,tv.tvDescripcion)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TipoVehiculo(cnxn, tv:TipoVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoVehiculo WHERE idTipoVehiculo = ?"
    data = (tv.idTipoVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TipoVehiculo(cnxn, tv:TipoVehiculo):
    cursor = cnxn.cursor()
    update_query = "UPDATE TipoVehiculo SET tcActivo = ? ,tcCodigoCombustible = ? ,tcNombre = ? WHERE idTipoVehiculo = ?"
    data = (tv.tcActivo,tv.tcCodigoCombustible,tv.tcNombre, tv.idTipoCombustible)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TipoVehiculo(cnxn,  tv:TipoVehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TipoVehiculo SET tcActivo = 0 WHERE idTipoVehiculo = ?"
    data = (tv.idTipoVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()