from Model.Entities import TipoCombustible


def todos_TipoCombustible(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoCombustible WHERE tcActivo = 1"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    return rows

def crear_registro_TipoCombustible(cnxn,tc:TipoCombustible):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TipoCombustible (tcActivo,tcCodigoCombustible,tcNombre) VALUES (?, ?, ?)"
    data = (tc.tcActivo,tc.tcCodigoCombustible,tc.tcNombre)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TipoCombustible(cnxn, tc:TipoCombustible):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoCombustible WHERE idTipoCombustible = ?"
    data = (tc.idTipoCombustible)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TipoCombustible(cnxn,tc:TipoCombustible):
    cursor = cnxn.cursor()
    update_query = "UPDATE TipoCombustible SET tcActivo = ? ,tcCodigoCombustible = ? ,tcNombre = ? WHERE idTipoCombustible = ?"
    data = ( tc.tcActivo,tc.tcCodigoCombustible,tc.tcNombre, tc.idTipoCombustible)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TipoCombustible(cnxn, tc:TipoCombustible):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TipoCombustible SET tcActivo = 0 WHERE idTipoCombustible = ?"
    data = (tc.idTipoCombustible)
    cursor.execute(delete_query, data)
    cnxn.commit()