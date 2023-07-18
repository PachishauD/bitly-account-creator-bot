import expressvpn
from requests import get

for i in range(0, 10):
    ip = get("https://api.ipify.org").content.decode("utf-8")
    print(ip)