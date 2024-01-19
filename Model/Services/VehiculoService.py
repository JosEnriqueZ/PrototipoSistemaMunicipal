def todos_Vehiculo(cnxn):
    cursor = cnxn.cursor()
    select_query = """
    SELECT Vehiculo.*, TipoVehiculo.tvNombre,TipoCombustible.tcNombre
        FROM Vehiculo 
        JOIN TipoVehiculo ON Vehiculo.tipoVehiculoFK = TipoVehiculo.idTipoVehiculo
        JOIN TipoCombustible ON Vehiculo.tipoCombustibleFK= TipoCombustible.idTipoCombustible where VehActivo = 1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def crear_registro_Vehiculo(cnxn,VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Vehiculo (VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible) VALUES (?, ?, ? ,?,?,?,?,?,?,?,?)"
    data = (VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Vehiculo(cnxn, idVehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Vehiculo WHERE idVehiculo = ?"
    data = (idVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Vehiculo(cnxn,VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible, idVehiculo):
    cursor = cnxn.cursor()
    update_query = "UPDATE Vehiculo SET VehActivo = ? ,tipoVehiculoFK = ? ,tipoCombustibleFK = ? ,VehColor = ? ,VehPeso = ? ,VehNumeroPlaca = ? ,VehMarca = ? ,VahAnio = ? ,VehRevisionTecnica = ? ,VehDescripcion = ? ,VehGalonesHoraCombustible = ? WHERE idVehiculo = ?"
    data = ( VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible, idVehiculo)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Vehiculo(cnxn, idVehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Vehiculo SET VehActivo = 0 WHERE idVehiculo = ?"
    data = (idVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()