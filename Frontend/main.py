import tkinter as tk
from ventanaPrincipal import VentanaPrincipal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.post("/create_item")
async def create_item(item: Item):
    # Operación de Crear (Create)
    # Agregar un nuevo elemento al archivo JSON
    with open('data.json', 'a') as f:
        json.dump(item.dict(), f)
        f.write('\n')
    return item

@app.get("/read_items")
async def read_items():
    # Operación de Leer (Read)
    # Leer todos los elementos del archivo JSON
    with open('data.json', 'r') as f:
        items = [json.loads(line) for line in f]
    return items

@app.put("/update_item/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    # Operación de Actualizar (Update)
    # Actualizar un elemento específico en el archivo JSON
    with open('data.json', 'r') as f:
        items = [json.loads(line) for line in f]

    if 0 <= item_id < len(items):
        items[item_id] = updated_item.dict()
        with open('data.json', 'w') as f:
            for item in items:
                json.dump(item, f)
                f.write('\n')
        return {"status": "success"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/delete_item/{item_id}")
async def delete_item(item_id: int):
    # Operación de Eliminar (Delete)
    # Eliminar un elemento específico del archivo JSON
    with open('data.json', 'r') as f:
        items = [json.loads(line) for line in f]

    if 0 <= item_id < len(items):
        del items[item_id]
        with open('data.json', 'w') as f:
            for item in items:
                json.dump(item, f)
                f.write('\n')
        return {"status": "success"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
