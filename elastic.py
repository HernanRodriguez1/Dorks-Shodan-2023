import argparse
import requests

def main(host):
    port = 9200

    # Construir la URL del endpoint _cat/indices?v
    indices_url = f"http://{host}:{port}/_cat/indices?v"

    # Realizar la solicitud GET para obtener los índices disponibles
    response = requests.get(indices_url)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        print("Índices disponibles:")
        print(response.text)

        # Solicitar al usuario que ingrese un índice
        index = input("\nIngresa el nombre del índice al que deseas acceder: ")

        # Construir la URL del endpoint _search?pretty= para el índice seleccionado
        search_url = f"http://{host}:{port}/{index}/_search?pretty="

        # Solicitar la consulta de búsqueda al usuario
        search_query = input("Ingresa la consulta de búsqueda: ")

        # Construir la URL completa para la búsqueda utilizando GET
        full_search_url = f"{search_url}{search_query}"

        # Realizar la solicitud GET para buscar en el índice seleccionado
        search_response = requests.get(full_search_url)

        # Verificar el estado de la respuesta
        if search_response.status_code == 200:
            print("Resultados de la búsqueda:")
            print(search_response.text)
        else:
            print("Error al realizar la búsqueda.")
    else:
        print("Error al obtener la lista de índices.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conectar y buscar en Elasticsearch")
    parser.add_argument("-t", "--host", type=str, required=True, help="Host de Elasticsearch")
    args = parser.parse_args()
    
    main(args.host)
