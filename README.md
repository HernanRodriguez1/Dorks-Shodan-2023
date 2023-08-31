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
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/ee3ab4a1-dd6c-48c6-a111-b31d156e1185)

```sh
curl -X GET "http://192.x.x.153:9200/.monitoring-beats-7-2023.08.30"
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/27f99c76-781d-4402-a1b5-b516e89f5db3)

```sh
curl -X GET "http://192.x.x.153:9200/_search?pretty=true"
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/8d106fb3-f0d7-4865-a9e6-839a04ddd2b7)



# Authentication Disabled SMB

```sh
"Authentication: disabled" port:445 product:"Samba" 
```
```sh
smbclient -L //200.x.x.29/ -N  
smbclient //200.x.x.29/info
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/da427f4b-0f7b-4f2b-9b0e-326da7e78420)
