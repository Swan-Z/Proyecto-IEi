import tkinter as tk
from busqueda import BuscadorCentros
from ventanaCarga import VentanaCarga

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("700x500")

        self.btn_carga = tk.Button(self.root, text="Ir a Carga", command=self.ir_a_carga)
        self.btn_carga.pack(pady=10)

        self.btn_busqueda = tk.Button(self.root, text="Ir a Búsqueda", command=self.ir_a_busqueda)
        self.btn_busqueda.pack(pady=10)

    def ir_a_carga(self):
        carga_window = VentanaCarga(self.root)

    def ir_a_busqueda(self):
        busqueda_root = tk.Tk()
        busqueda_window = BuscadorCentros(busqueda_root)
        busqueda_root.mainloop()

root = tk.Tk()
app = VentanaPrincipal(root)

root.mainloop()
