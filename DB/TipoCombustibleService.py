def todos_TipoCombustible(cnxn):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoCombustible"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print(rows)
    return rows

def crear_registro_TipoCombustible(cnxn,tcActivo,tcCodigoCombustible,tcNombre):
    cursor = cnxn.cursor()
    insert_query = "INSERT INTO TipoCombustible (tcActivo,tcCodigoCombustible,tcNombre) VALUES (?, ?, ?)"
    data = (tcActivo,tcCodigoCombustible,tcNombre)
    cursor.execute(insert_query, data)
    cnxn.commit()

def leer_registro_TipoCombustible(cnxn, idTipoCombustible):
    cursor = cnxn.cursor()
    select_query = "SELECT * FROM TipoCombustible WHERE idTipoCombustible = ?"
    data = (idTipoCombustible,)
    cursor.execute(select_query, data)
    row = cursor.fetchone()
    return row

def actualizar_registro_TipoCombustible(cnxn,tcActivo,tcCodigoCombustible,tcNombre, idTipoCombustible):
    cursor = cnxn.cursor()
    update_query = "UPDATE TipoCombustible SET tcActivo = ? tcCodigoCombustible = ? tcNombre = ? WHERE idTipoCombustible = ?"
    data = ( tcActivo,tcCodigoCombustible,tcNombre, idTipoCombustible)
    cursor.execute(update_query, data)
    cnxn.commit()

def eliminar_registro_TipoCombustible(cnxn, idTipoCombustible):
    cursor = cnxn.cursor()
    delete_query = "UPDATE TipoCombustible SET tcActivo = 0 WHERE idTipoCombustible = ?"
    data = (idTipoCombustible)
    cursor.execute(delete_query, data)
    cnxn.commit()