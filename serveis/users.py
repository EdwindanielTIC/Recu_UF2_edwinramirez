
def inserirusuarios(nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password):
    conn = coneccion_db()
    cur = conn.cursor()
    sql = "INSET INTO users (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password)
    cur.execute(sql,(values,))
    conn.commit()
    cur.close()
    return {"msg": "Usuario incertado correctamente"}