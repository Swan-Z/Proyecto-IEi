import tkinter as tk

class VentanaCarga:
    def __init__(self, master):
        self.master = master
        self.ventana_carga = tk.Toplevel(master)
        self.ventana_carga.title("API de carga")
        self.textfield = tk.Entry(self.ventana_carga)
        self.textfield.pack(pady=10)

        self.boton_volver = tk.Button(self.ventana_carga, text="Volver a Principal", command=self.volver_a_principal)
        self.boton_volver.pack(pady=10)

    def volver_a_principal(self):
        self.ventana_carga.destroy()