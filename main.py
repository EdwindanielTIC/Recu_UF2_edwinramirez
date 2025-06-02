## añado ejercicio 5
from fastapi import FastAPI

app = FastAPI()

@app.put("/actualizarUser", response_model= dict)
async def actualizarUser(cognom ,direcció):
    dadesActualizar = query.actualizarUser(cognom,direcció)
    return dadesActualizar

