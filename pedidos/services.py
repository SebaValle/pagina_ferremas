import requests

def consultar_dolar_actual():
    """
    Consumo real de API mindicador.cl
    Incluye manejo de excepciones (Punto requerido en el avance)
    """
    url = "https://mindicador.cl/api/dolar"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Verifica si hubo error HTTP
        data = response.json()
        return float(data['serie'][0]['valor'])
    except Exception as e:
        print(f"Error en API externa: {e}")
        # Valor por defecto si la API falla para no detener la orquestación
        return 950.0