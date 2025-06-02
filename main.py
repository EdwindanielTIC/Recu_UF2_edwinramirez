from typing import List
from fastapi import FastAPI
import serveis.users as query

app = FastAPI()

@app.post("/Users",response_model=dict)
async def inserirUsuaris(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password):
    users = query.inserirusuarios(nombre,apellido,correo,descripcion,curso,año,direccion,codigoP,password)
    return users

@app.get("/getUsuarios",response_model=List[dict])
async def obtenerUsuarios(nombre,cognom,correo,curso,any,direccio):
    usuarios = query.selecionarUsuario(nombre,cognom,correo,curso,any,direccio)
    return usuarios

