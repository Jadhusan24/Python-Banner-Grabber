from banner import get_headers
from banner import grab_banner

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