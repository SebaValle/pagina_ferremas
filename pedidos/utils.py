import requests

def obtener_valor_dolar():
    """
    Consume la API externa de mindicador.cl para obtener el valor del dólar actual.
    Incluye manejo de errores para cumplir con la pauta.
    """
    url = "https://mindicador.cl/api/dolar"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Lanza error si la API externa falla
        data = response.json()
        return float(data['serie'][0]['valor'])
    except Exception as e:
        print(f"Error consultando API externa: {e}")
        return None # Manejo de excepción: si falla, devolvemos None