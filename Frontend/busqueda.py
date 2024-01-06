import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Buscador de centros educativos")
root.geometry("700x500")

def cancelar():
    # Añadir cualquier lógica necesaria para cancelar aquí
    print("Cancelando...")

def buscar():
    # Añadir cualquier lógica necesaria para buscar aquí
    print("Buscando...")

titulo = tk.Label(root, text="Buscador de centros educativos", font=("", 16))
titulo.pack(pady=30)

label_width = 15  # Ancho común para todos los labels

# Localidad
frame_localidad = tk.Frame(root)
frame_localidad.pack(pady=10)

label_localidad = tk.Label(frame_localidad, text="Localidad:", width=label_width)
label_localidad.pack(side=tk.LEFT, padx=(10, 10))

entry_localidad = tk.Entry(frame_localidad, width=23)
entry_localidad.pack(side=tk.LEFT)

# Código Postal
frame_codigo_postal = tk.Frame(root)
frame_codigo_postal.pack(pady=10)

label_codigo_postal = tk.Label(frame_codigo_postal, text="Código Postal:", width=label_width)
label_codigo_postal.pack(side=tk.LEFT, padx=(10, 10))

entry_codigo_postal = tk.Entry(frame_codigo_postal, width=23)
entry_codigo_postal.pack(side=tk.LEFT)

# Provincia
frame_provincia = tk.Frame(root)
frame_provincia.pack(pady=10)

label_provincia = tk.Label(frame_provincia, text="Provincia:", width=label_width)
label_provincia.pack(side=tk.LEFT, padx=(10, 10))

entry_provincia = tk.Entry(frame_provincia, width=23)
entry_provincia.pack(side=tk.LEFT)

# Tipo (Choice Box)
frame_tipo = tk.Frame(root)
frame_tipo.pack(pady=10)

label_tipo = tk.Label(frame_tipo, text="Tipo:", width=label_width)
label_tipo.pack(side=tk.LEFT, padx=(10, 10))

tipo_values = ["Público", "Privado", "Concertado", "Otro"]
entry_tipo = ttk.Combobox(frame_tipo, values=tipo_values)
entry_tipo.pack(side=tk.LEFT)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

button_cancelar = tk.Button(frame_botones, text="Cancelar", command=cancelar)
button_cancelar.pack(side=tk.LEFT, padx=(0, 55))

button_buscar = tk.Button(frame_botones, text="Buscar", command=buscar)
button_buscar.pack(side=tk.LEFT)

root.mainloop()
