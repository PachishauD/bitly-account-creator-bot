import expressvpn
import time

from requests import get
from expressvpn import wrapper


for i in range(0, 10):
    time.sleep(3)
    wrapper.random_connect(True)
    ip = get("https://api.ipify.org").content.decode("utf-8")
    print(ip)