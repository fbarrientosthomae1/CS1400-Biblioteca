"""
Módulo para manejar las comunicaciones externas con WeatherAPI.
Optimizado para el laboratorio CS1400 de la Universidad Weber.
"""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# --- CONFIGURACIÓN DE RUTAS ---
# Esto busca el archivo .env subiendo desde: src/weather_wizard/api.py -> src -> raíz
ruta_base = Path(__file__).resolve().parent.parent.parent
ruta_env = ruta_base / '.env'

# Cargamos el archivo .env forzando la ruta absoluta
load_dotenv(dotenv_path=ruta_env)

# --- VARIABLES DE ENTORNO ---
BASE_URL = "https://api.weatherapi.com/v1/current.json"
# Usamos el nombre exacto que tienes en tu archivo: WEATHER_API_KEY
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather_from_provider(city_name: str) -> dict:
    """
    Realiza una petición HTTP GET a WeatherAPI para obtener el clima.
    """
    
    # Verificación de seguridad para la tarea
    if not API_KEY or "tu_llave" in API_KEY:
        raise ConnectionError(f"Error: No se encontró la llave en {ruta_env}. Revisa tu archivo .env")

    parametros = {
        "key": API_KEY,
        "q": city_name,
        "lang": "es"
    }

    try:
        respuesta = requests.get(BASE_URL, params=parametros, timeout=10)
        
        # Si la API responde con error 400 (Ciudad no encontrada) o 403 (Llave inválida)
        if respuesta.status_code == 400:
            raise ValueError(f"No pudimos encontrar la ciudad: {city_name}")
        elif respuesta.status_code == 403:
            raise ConnectionError("Error: La API KEY no es válida o ha expirado.")
            
        respuesta.raise_for_status()
        return respuesta.json()

    except requests.exceptions.HTTPError as e:
        raise ValueError(f"Error del servidor: {e}")
    except requests.exceptions.RequestException:
        raise ConnectionError("Error de red: Revisa tu conexión a internet.")