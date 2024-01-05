import tkinter as tk

class VentanaBusqueda:
    def __init__(self, master):
        self.master = master
        self.ventana_busqueda = tk.Toplevel(self.master)
        self.ventana_busqueda.title("API de búsqueda")

        self.textfield = tk.Entry(self.ventana_busqueda)
        self.textfield.pack(pady=10)

        self.boton_volver_ventana2 = tk.Button(self.ventana_busqueda, text="Volver a Principal", command=self.volver_a_principal)
        self.boton_volver_ventana2.pack(pady=10)

    def volver_a_principal(self):
        self.ventana_busqueda.destroy()
