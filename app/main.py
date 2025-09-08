from fastapi import FASTAPI, Request
import os

app = FastAPI()
DATA_FILE = "/data/notas.txt"

@app.post("/nota")
async def guardar_nota(Request):
    nota = await Request.body()
    with open(DATA_FILE, "a") as f:
        f.write(nota.decode() + "\\n")
    return {"mensaje": "nota guardada"}

@app.get("/")
def leer_notas():
    if not os.path.exists(DATA_FILE):
        return {"notas": []}
    with open(DATA_FILE, "r") as f:
        return {"notas": f.read().splitlines()}