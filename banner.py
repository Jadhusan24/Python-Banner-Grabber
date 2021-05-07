import socket
import requests

def get_headers(url):
    resp = ''
    if url.startswith('http') or url.startswith('https'):
        pass
    else:
        url = 'http://'+url
    try:
        resp = requests.get(url)
        return (80, resp.headers)
    except requests.exceptions.MissingSchema as e:
        print(e)
        return None


def grab_banner(target: str, port: int, timeout=10.0):
    if port == 80:
        return get_headers(target)
    s = socket.socket()
    try:
        if target.startswith('http'):
            target = target.split("//")[1]
        s.connect((target, port))
        s.settimeout(timeout)  # stop connection
        banner = str(s.recv(1024).strip('b'))
        return (port, banner)
    except Exception as e:
        print(e)
        return s.close()

def main(ports: list, target: str):
    banners = []
    for port in ports:
        banner = grab_banner(target, int(port))
        if banner:
            banners.append(banner)
    print(f"Target : {target}")
    print("Banners: ", banners)


ports = input("Enter ports (seperated by ,) > ").split(",")
target = input("Enter target URL or domain > ")
main(ports, target)
