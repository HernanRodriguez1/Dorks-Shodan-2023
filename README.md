# Dorks Shodan 2023

Recopilación de Querys de shodan con scripts personalizados :)

# DICOM 
El estándar DICOM (Digital Imaging and Communications in Medicine) es un estándar utilizado en la industria médica para la gestión, almacenamiento y transmisión de imágenes médicas, como radiografías, tomografías computarizadas (TC), imágenes de resonancia magnética (IRM), entre otras.

```sh
"DICOM Server Response" port:104
```
```sh
python3 Dicom.py
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/29f923e0-fbde-4526-a199-fbf71cb5319f)

# Elasticsearch
Elasticsearch es un motor de búsqueda y análisis distribuido, de código abierto, basado en Lucene. Se utiliza para indexar, buscar y analizar grandes volúmenes de datos en tiempo real. Está diseñado para manejar datos no estructurados o semiestructurados y es especialmente útil para casos de uso en los que se requiere búsqueda y análisis de texto, logística, monitoreo y análisis de registros, y más

```sh
port:"9200" elastic: "Total Size:"
```
```sh
curl -X GET "http://192.x.x.153:9200/_cat/indices?v"
curl -X GET "http://192.x.x.153:9200/.monitoring-beats-7-2023.08.30"
curl -X GET "http://192.x.x.153:9200/_search?pretty=true"
```

```sh
python3 elastic.py -t 192.x.x.153
```
![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/25dadba2-91d2-4bc6-9a91-6c238120d557)


## Access FTP Anonymous
El acceso FTP anónimo es una forma de conectarse a un servidor FTP sin proporcionar credenciales de autenticación específicas.

```sh
"220" "230 Login successful." port:21
230 'anonymous@' login ok 
"Anonymous+access+allowed" port:"21"
```

```sh
shodan search :"220" "230 Login successful." port:21 --fields ip_str --separator " " | awk '{print $1}' | cat > ips.txt
```
```sh
python3 ftp.py -l ips.txt
```
![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/59945aef-9d89-4c2d-bbc6-a876ad1ed68d)


# Authentication Disabled SMB
La autenticación SMB (Server Message Block) sin credenciales, también conocida como acceso SMB anónimo, permite a los usuarios acceder a recursos compartidos en una red sin proporcionar nombres de usuario ni contraseñas. Esto puede ser útil para acceder a carpetas compartidas que se han configurado para permitir el acceso anónimo.

```sh
"Authentication: disabled" port:445 product:"Samba" 
```
```sh
smbclient -L //200.x.x.29/ -N  
smbclient //200.x.x.29/info
```
![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/da427f4b-0f7b-4f2b-9b0e-326da7e78420)

## Access authentication disabled VNC
Esto significa que el servidor VNC está configurado para permitir conexiones sin requerir autenticación.

```sh
"authentication disabled" port:5900,5901
```
```sh
vncviewer -passwd none 91.x.x.238
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/9e610141-1ccf-4388-92c5-c824704ca9c0)



