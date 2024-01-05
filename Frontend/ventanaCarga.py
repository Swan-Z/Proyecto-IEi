import tkinter as tk

class VentanaCarga:
    def __init__(self, master):
        self.master = master
        self.ventana_carga = tk.Toplevel(master)
        self.ventana_carga.title("API de carga")
        self.ventana_carga.geometry("900x700")

        self.titulo = tk.Label(self.ventana_carga, text="Buscador de centros educativos", font=("Arial",20))
        self.titulo.pack(pady=(100,40))

        frame_grid = tk.Frame(self.ventana_carga)
        frame_grid.pack()

        self.labelLocalidad = tk.Label(frame_grid, text="Localidad:")
        self.labelLocalidad.grid(row=0, column=0, padx=10, sticky='W')
        self.textFieldlocalidad = tk.Entry(frame_grid)
        self.textFieldlocalidad.grid(row=0, column=1, padx=10, sticky='W')
        

        self.boton_volver = tk.Button(self.ventana_carga, text="Volver a Principal", command=self.volver_a_principal)
        self.boton_volver.pack(pady=10)

    def volver_a_principal(self):
        self.ventana_carga.destroy()