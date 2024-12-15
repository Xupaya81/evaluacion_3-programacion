import requests
from Modelos.posts import Post
from Auxiliares.construir_url import url_servicio

def obtener_posts_api():
    direccion = url_servicio("posts")  # reutilizacion de la funcion url_de servicio
    try:
        respuesta = requests.get(direccion)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()
    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")

    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")

    except requests.exceptions.RequestException as error:
        print(f"Error en la solicitud: {error}")
