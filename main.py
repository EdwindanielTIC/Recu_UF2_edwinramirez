from fastapi import FastAPI
import serveis.users as query

app = FastAPI()


@app.post("/Users",response_model=dict)
async def inserirUsuaris(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password):
    users = query.inserirusuarios(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password)
    return users
