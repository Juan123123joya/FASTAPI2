import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

class Libro(BaseModel):
    título: str
    autor: str
    paginas: int
    editorial: Optional [str]
@app.get("/")
def index():
    return {"message": "Hola, Pythonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}    

@app.post("/Libros")
def insertar_Libro(libro: Libro):
    return {"message" : f"Libro {libro.título} insertado"}

