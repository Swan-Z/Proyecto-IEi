import tkinter as tk

def cargar_datos():
    # Lógica para cargar los datos desde la fuente seleccionada
    # En este ejemplo, simplemente agregamos texto a la lista
    resultados = ["Dato 1", "Dato 2", "Dato 3"]

    # Limpiar el contenedor antes de agregar los nuevos datos
    for widget in contenedor.winfo_children():
        widget.destroy()

    # Mostrar los resultados en el contenedor
    for resultado in resultados:
        label_resultado = tk.Label(contenedor, text=resultado)
        label_resultado.pack()

def cancelar():
    # Lógica para cancelar la operación
    pass

root = tk.Tk()
root.title("Interfaz de carga de datos")

# Etiqueta grande
label_titulo = tk.Label(root, text="Carga de almacen de datos", font=("Arial", 18))
label_titulo.pack()

# Etiqueta "Seleccionar fuente"
label_seleccion = tk.Label(root, text="Seleccionar fuente:")
label_seleccion.pack()

# Checkbuttons para las opciones
opciones = ["Seleccionar todas", "Murcia", "Comunidad Valenciana", "Cataluña"]
fuente_seleccionada = []
for opcion in opciones:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=opcion, variable=var)
    checkbox.pack()
    fuente_seleccionada.append((opcion, var))

# Botones de cancelar y cargar
frame_botones = tk.Frame(root)
frame_botones.pack()
boton_cancelar = tk.Button(frame_botones, text="Cancelar", command=cancelar)
boton_cancelar.pack(side=tk.LEFT)
boton_cargar = tk.Button(frame_botones, text="Cargar", command=cargar_datos)
boton_cargar.pack(side=tk.LEFT)

# Etiqueta "Resultados de la carga"
label_resultados = tk.Label(root, text="Resultados de la carga:")
label_resultados.pack()

# Contenedor para mostrar los resultados
contenedor = tk.Frame(root)
contenedor.pack()

root.mainloop()