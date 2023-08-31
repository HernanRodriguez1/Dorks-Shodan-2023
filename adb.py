import subprocess

with open('ips.txt', 'r') as ip_file:
    for line in ip_file:
        ip = line.strip()
        print(ip)
        subprocess.run(['adb', 'connect', f'{ip}:5555'])
