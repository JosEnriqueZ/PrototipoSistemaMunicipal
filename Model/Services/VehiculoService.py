from Model.Entities.Vehiculo import Vehiculo

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

def crear_registro_Vehiculo(cnxn,v:Vehiculo):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Vehiculo (VehActivo,tipoVehiculoFK,tipoCombustibleFK,VehColor,VehPeso,VehNumeroPlaca,VehMarca,VahAnio,VehRevisionTecnica,VehDescripcion,VehGalonesHoraCombustible) VALUES (?, ?, ? ,?,?,?,?,?,?,?,?)"
    data = (v.VehActivo,v.tipoVehiculoFK,v.tipoCombustibleFK,v.VehColor,v.VehPeso,v.VehNumeroPlaca,v.VehMarca,v.VahAnio,v.VehRevisionTecnica,v.VehDescripcion,v.VehGalonesHoraCombustible)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Vehiculo(cnxn, v:Vehiculo):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Vehiculo WHERE idVehiculo = ?"
    data = (v.idVehiculo,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Vehiculo(cnxn,v:Vehiculo):
    cursor = cnxn.cursor()
    update_query = """UPDATE Vehiculo SET VehActivo = ? ,
                    tipoVehiculoFK = ? ,tipoCombustibleFK = ? ,
                    VehColor = ? ,VehPeso = ? ,VehNumeroPlaca = ? ,
                    VehMarca = ? ,VahAnio = ? ,VehRevisionTecnica = ? ,
                    VehDescripcion = ? ,VehGalonesHoraCombustible = ? 
                    WHERE idVehiculo = ?"""
    data = ( v.VehActivo,v.tipoVehiculoFK,v.tipoCombustibleFK,v.VehColor,
            v.VehPeso,v.VehNumeroPlaca,v.VehMarca,v.VahAnio,v.VehRevisionTecnica,
            v.VehDescripcion,v.VehGalonesHoraCombustible, v.idVehiculo)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Vehiculo(cnxn, v:Vehiculo):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Vehiculo SET VehActivo = 0 WHERE idVehiculo = ?"
    data = (v.idVehiculo)
    cursor.execute(delete_query, data)
    cnxn.commit()