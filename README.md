# Exploits-Shodan

Recopilación de Querys de shodan con exploits :)

## DICOM 

```sh
"DICOM Server Response" port:104
```

## Exploit:

```sh
python3 Dicom.py
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/29f923e0-fbde-4526-a199-fbf71cb5319f)

## Authentication Disabled SMB

```sh
"Authentication: disabled" port:445 product:"Samba" 
```
## Access:

```sh
smbclient -L //200.x.x.29/ -N  
smbclient //200.x.x.29/info
```

![image](https://github.com/HernanRodriguez1/Exploits-Shodan/assets/66162160/da427f4b-0f7b-4f2b-9b0e-326da7e78420)
