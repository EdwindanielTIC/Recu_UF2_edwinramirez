from typing import List
from fastapi import FastAPI
import serveis.users as query
import Schema.user_sch as schema


app = FastAPI()

@app.post("/Users",response_model=dict)
async def inserirUsuaris(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password):
    users = query.inserirusuarios(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password)
    return users

@app.get("/getUsuarios",response_model=List[dict])
async def obtenerUsuarios(nombre,cognom,correo,curso,any,direccio):
    usuarios = query.selecionarUsuario(nombre,cognom,correo,curso,any,direccio)
    return schema.users_schema(usuarios)


## añado ejercicio 5

@app.put("/actualizarUser", response_model=dict)
async def actualizarUser(id,cognom ,direcció):
    dadesActualizar = query.actualizar(id,cognom,direcció)
    return dadesActualizar


##ejercicio6
@app.delete("/EliminarUser", response_model=dict)
async def eliminarUsuario(iduser):
    usereliminar = query.eliminarUsuario(iduser)
    return usereliminar

