# import expressvpn
# import time

# from requests import get
# from expressvpn import wrapper


# for i in range(0, 10):
#     time.sleep(3)
#     wrapper.random_connect(True)
#     ip = get("https://api.ipify.org").content.decode("utf-8")
#     print(ip)
import sys
import os

# Check if virtual environment is active
if not hasattr(sys, 'real_prefix') and 'VIRTUAL_ENV' not in os.environ:
    print('Please activate virtual environment before running this script')
    sys.exit(1)
else:
    print("hehe")
