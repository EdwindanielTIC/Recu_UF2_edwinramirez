from config.database import connection_db

def inserirusuarios(nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password):
    conn = connection_db()
    cur = conn.cursor()
    sql = "INSERT INTO users (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (nombre,cogno,correo,descripcion,curso,any,direccio,codgiP,password)
    cur.execute(sql,(values))
    conn.commit()
    cur.close()
    return {"msg": "Usuario incertado correctamente"}