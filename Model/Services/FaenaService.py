from Model.Entities.Faena import Faena
from Model.Entities.Vehiculo import Vehiculo


def todos_faenas(cnxn):
    cursor = cnxn.cursor()
    select_query = """
        SELECT f.*, t.trabNombre, u.usuName ,CONCAT(v.VehNumeroPlaca,' - ',v.idVehiculo) FROM Faena as f
        left join Trabajador    as t on t.idTrabajador    = f.idTrabajadorFK
        left join Vehiculo        as v on v.idVehiculo    = f.idVehiculoFK
        left join Usuario        as u on u.idUsuario        = f.idUsuarioFK where f.faenaActivo=1"""
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_Faena(cnxn, f:Faena):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO Faena (faenaActivo,idTrabajadorFK, idUsuarioFK, idVehiculoFK,faenaFechaTrabajo, faenaHoras, faenaRegion, faenaDescripcion, faenaDireccionTrabajo,faenaKilometrosAreaTrabajo) VALUES (?, ?, ?, ? , ?, ?, ?, ?, ?, ?)"
    data = (f.faenaActivo, f.idTrabajadorFK, f.idUsuarioFK, f.idVehiculoFK, f.faenaFechaTrabajo, f.faenaHoras, f.faenaRegion, f.faenaDescripcion, f.faenaDireccionTrabajo,f.faenaKilometrosAreaTrabajo)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_Faena(cnxn, f:Faena):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM Faena WHERE idFaena = ?"
    data = (f.idTrabajador,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_Faena(cnxn, f:Faena):
    cursor = cnxn.cursor()
    update_query = "UPDATE Faena SET faenaActivo = ? ,idTrabajadorFK = ? ,idUsuarioFK = ? ,idVehiculoFK = ? ,faenaFechaTrabajo = ? ,faenaHoras = ? ,faenaRegion = ? ,faenaDescripcion = ? ,faenaDireccionTrabajo = ? ,faenaKilometrosAreaTrabajo = ? WHERE idFaena = ?"
    data = ( f.faenaActivo, f.idTrabajadorFK, f.idUsuarioFK, f.idVehiculoFK, f.faenaFechaTrabajo, f.faenaHoras, f.faenaRegion, f.faenaDescripcion, f.faenaDireccionTrabajo,f.faenaKilometrosAreaTrabajo, f.idFaena)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_Faena(cnxn, f:Faena):
    cursor = cnxn.cursor()
    delete_query = "UPDATE Faena SET faenaActivo = 0 WHERE idFaena = ?"
    data = (f.idFaena)
    cursor.execute(delete_query, data)
    cnxn.commit()

def leer_registro_FaenaTotalReporte(cnxn):
    cursor = cnxn.cursor()
    select_query = """Select f.faenaFechaTrabajo, CONCAT(v.VehNumeroPlaca,'/',tv.tvNombre,' - ',v.VehColor,' - ',v.VehMarca) as DatosAuto, CONCAT(t.trabDNI,' - ',t.trabApellido,' - ',t.trabNombre,' - ',t.trabLicenciaConducir)as DatosPersona 
    from Faena as f
    left join Vehiculo as v on v.idVehiculo    = f.idVehiculoFK
    left join Trabajador as t on t.idTrabajador    = f.idTrabajadorFK
    left join TipoVehiculo as tv on tv.idTipoVehiculo = v.tipoVehiculoFK"""   
    cursor.execute(select_query)
    rows = cursor.fetchall()
    return rows

def leer_registro_FaenaxFecha(cnxn, fecha):
    cursor = cnxn.cursor()
    select_query = """Select f.faenaFechaTrabajo, CONCAT(v.VehNumeroPlaca,'/',tv.tvNombre,' - ',v.VehColor,' - ',v.VehMarca), CONCAT(t.trabDNI,' - ',t.trabApellido,' - ',t.trabNombre,' - ',t.trabLicenciaConducir) 
    from Faena as f
    left join Vehiculo as v on v.idVehiculo    = f.idVehiculoFK
    left join Trabajador as t on t.idTrabajador    = f.idTrabajadorFK
    left join TipoVehiculo as tv on tv.idTipoVehiculo = v.tipoVehiculoFK
    where f.faenaFechaTrabajo = ?"""   
    data = (fecha)
    cursor.execute(select_query, data)
    rows = cursor.fetchall()
    return rows
 

def leer_registro_FaenaxVehiculo(cnxn, idvehiculo):
    cursor = cnxn.cursor()
    select_query = """Select f.faenaFechaTrabajo, CONCAT(v.VehNumeroPlaca,'/',tv.tvNombre,' - ',v.VehColor,' - ',v.VehMarca), CONCAT(t.trabDNI,' - ',t.trabApellido,' - ',t.trabNombre,' - ',t.trabLicenciaConducir) 
    from Faena as f
    left join Vehiculo as v on v.idVehiculo    = f.idVehiculoFK
    left join Trabajador as t on t.idTrabajador    = f.idTrabajadorFK
    left join TipoVehiculo as tv on tv.idTipoVehiculo = v.tipoVehiculoFK
    where v.idVehiculo =  ?"""   
    data = (idvehiculo)
    cursor.execute(select_query, data)
    rows = cursor.fetchall()
    return rows