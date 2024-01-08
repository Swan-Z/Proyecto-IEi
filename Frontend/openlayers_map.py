# openlayers_map.py

from openlayers import Map, View, TileLayer

class OpenLayersMap:
    def __init__(self, target_id):
        self.map = Map(
            target=target_id,  # ID del contenedor del mapa en tu HTML
            layers=[TileLayer(source="OSM")],  # Capa de mapa base (puedes ajustarla)
            view=View(center=[0, 0], zoom=2)  # Configuración inicial del mapa
        )

    def get_map(self):
        return self.map
