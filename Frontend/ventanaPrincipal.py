import tkinter as tk
import ventanaCarga as vc
import ventanaBusqueda as vb


class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")
        self.boton_carga = tk.Button(self.master, text="API Carga", command=self.abrir_ventana_carga)
        self.boton_carga.pack(pady=10)
        self.boton_busqueda = tk.Button(self.master, text="API Busqueda", command=self.abrir_ventana_busqueda)
        self.boton_busqueda.pack(pady=10)
    
    def abrir_ventana_carga(self):
        self.ventanaCarga = vc.VentanaCarga(self.master)
        
    def abrir_ventana_busqueda(self):
        self.ventanaBusqueda = vb.VentanaBusqueda(self.master)