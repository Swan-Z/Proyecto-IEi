import tkinter as tk
from tkinter import ttk

class BuscadorCentros:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador de centros educativos")
        self.root.geometry("700x500")

        self.create_widgets()

    def create_widgets(self):
        titulo = tk.Label(self.root, text="Buscador de centros educativos", font=("", 16))
        titulo.pack(pady=30)

        label_width = 15  # Ancho común para todos los labels

        # Localidad
        frame_localidad = tk.Frame(self.root)
        frame_localidad.pack(pady=10)

        label_localidad = tk.Label(frame_localidad, text="Localidad:", width=label_width)
        label_localidad.pack(side=tk.LEFT, padx=(10, 10))

        self.entry_localidad = tk.Entry(frame_localidad, width=23)
        self.entry_localidad.pack(side=tk.LEFT)

        # Código Postal
        frame_codigo_postal = tk.Frame(self.root)
        frame_codigo_postal.pack(pady=10)

        label_codigo_postal = tk.Label(frame_codigo_postal, text="Código Postal:", width=label_width)
        label_codigo_postal.pack(side=tk.LEFT, padx=(10, 10))

        self.entry_codigo_postal = tk.Entry(frame_codigo_postal, width=23)
        self.entry_codigo_postal.pack(side=tk.LEFT)

        # Provincia
        frame_provincia = tk.Frame(self.root)
        frame_provincia.pack(pady=10)

        label_provincia = tk.Label(frame_provincia, text="Provincia:", width=label_width)
        label_provincia.pack(side=tk.LEFT, padx=(10, 10))

        self.entry_provincia = tk.Entry(frame_provincia, width=23)
        self.entry_provincia.pack(side=tk.LEFT)

        # Tipo (Choice Box)
        frame_tipo = tk.Frame(self.root)
        frame_tipo.pack(pady=10)

        label_tipo = tk.Label(frame_tipo, text="Tipo:", width=label_width)
        label_tipo.pack(side=tk.LEFT, padx=(10, 10))

        tipo_values = ["Público", "Privado", "Concertado", "Otro"]
        self.entry_tipo = ttk.Combobox(frame_tipo, values=tipo_values)
        self.entry_tipo.pack(side=tk.LEFT)

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        button_cancelar = tk.Button(frame_botones, text="Cancelar", command=self.cancelar)
        button_cancelar.pack(side=tk.LEFT, padx=(0, 55))

        button_buscar = tk.Button(frame_botones, text="Buscar", command=self.buscar)
        button_buscar.pack(side=tk.LEFT)

    def obtener_valores(self):
        localidad = self.entry_localidad.get()
        codigo_postal = self.entry_codigo_postal.get()
        provincia = self.entry_provincia.get()
        tipo = self.entry_tipo.get()

        return localidad, codigo_postal, provincia, tipo

    def cancelar(self):
        # Borra los textos de los Entry
        self.entry_localidad.delete(0, tk.END)
        self.entry_codigo_postal.delete(0, tk.END)
        self.entry_provincia.delete(0, tk.END)
        self.entry_tipo.set("")  # Borra la selección del Combobox

        print("Cancelando...")

    def buscar(self):
        localidad, codigo_postal, provincia, tipo = self.obtener_valores()
        # Añadir cualquier lógica necesaria para buscar aquí
        print("Buscando...")
        print("Localidad:", localidad)
        print("Código Postal:", codigo_postal)
        print("Provincia:", provincia)
        print("Tipo:", tipo)

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorCentros(root)
    root.mainloop()
