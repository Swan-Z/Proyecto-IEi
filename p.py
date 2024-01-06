from flask import Flask, render_template, request
import folium

app = Flask(__name__)

locations = []  # Lista para almacenar las ubicaciones

@app.route('/')
def index():
    return render_template('index.html', locations=locations, map_html='')

@app.route('/search', methods=['POST'])
def search():
    try:
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        location_name = request.form['location_name']

        # Verificar que las coordenadas estén en el rango válido
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            locations.append({'name': location_name, 'lat': lat, 'lon': lon})

            # Crear el mapa con todas las ubicaciones
            map = folium.Map(location=[lat, lon], zoom_start=10)
            for loc in locations:
                folium.Marker([loc['lat'], loc['lon']], popup=f"{loc['name']} ({loc['lat']}, {loc['lon']})").add_to(map)

            # Convertir el mapa a HTML y pasarlo como cadena
            map_html = map.get_root().render()

            return render_template('index.html', locations=locations, map_html=map_html)
        else:
            return render_template('index.html', locations=locations, map_html='', error_message='Coordenadas inválidas.')
    except ValueError:
        return render_template('index.html', locations=locations, map_html='', error_message='Ingresa valores numéricos para latitud y longitud.')

if __name__ == '__main__':
    app.run(debug=True)
