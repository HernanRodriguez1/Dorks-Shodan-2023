import argparse
import requests

def main(host):
    port = 9200

    indices_url = f"http://{host}:{port}/_cat/indices?v"
    response = requests.get(indices_url)

    if response.status_code == 200:
        print("Índices disponibles:")
        print(response.text)

        index = input("\nIngresa el nombre del índice al que deseas acceder: ")
        search_url = f"http://{host}:{port}/{index}/_search?pretty="
        search_query = input("Ingresa la consulta de búsqueda: ")
        full_search_url = f"{search_url}{search_query}"
        search_response = requests.get(full_search_url)

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
