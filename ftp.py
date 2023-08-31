import argparse
from ftplib import FTP

def ftp_connect(host, result):
    try:
        ftp = FTP(host)
        ftp.login("anonymous", "")
        ftp.quit()
        result[host] = "Éxito: Conexión anónima exitosa"
    except Exception as e:
        result[host] = f"Fallo: {str(e)}"

def main(list_file):
    with open(list_file, "r") as f:
        hosts = f.read().splitlines()

    results = {}

    for host in hosts:
        ftp_connect(host, results)
        print(f"{host}: {results[host]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conexión anónima a múltiples servidores FTP")
    parser.add_argument("-l", "--list", type=str, required=True, help="Archivo con lista de servidores")
    args = parser.parse_args()

    main(args.list)
