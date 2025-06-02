
def inserirusuarios(nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password):
    conn = connection_db()
    cur = conn.cursor()
    sql = "INSET INTO users (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password)
    cur.execute(sql,(values))
    conn.commit()
    cur.close()
    return {"msg": "Usuario incertado correctamente"}


def selecionarUsuario(nombre,cognom,correo,curso,any,direccio):
    conn = connection_db()
    cur = conn.cursor()
    sql = "SELECT nombre,cognom,correo,curso,any,direccio FROM users"
    cur.execute(sql,nombre,cognom,correo,curso,any,direccio)
    devolverUsers = cur.fetchall()
    conn.close()
    cur.close()
    return devolverUsers




