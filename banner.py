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