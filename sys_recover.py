import json
import socket
import os

SHADOWSOCKS_CONFIG = "/etc/shadowsocks.json"

def get_host_ip():
   try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      s.connect(('8.8.8.8', 80))
      ip = s.getsockname()[0]
   finally:
      s.close()
   return ip



def config_system():
    address = get_host_ip()

    data = {}

    print("Please input the password for the ss server : ")
    password = input()

    data["server"] = str(address)
    data["port_password"] = {}
    data["port_password"]["8381"] = password
    data["port_password"]["8382"] = password
    data["port_password"]["8383"] = password
    data["port_password"]["8386"] = password
    data["port_password"]["8388"] = password

    data["timeout"] = 600
    data["method"] = "aes-256-cfb"
    data["fast_open"] = "false"

    f = open(SHADOWSOCKS_CONFIG, "w")
    f.write(json.dumps(data, ensure_ascii=False, indent=4, separators=(",", ":")))
    f.close()

    os.system("apt-get install shadowsocks")
    os.system("service shadowsocks start")
    os.system("ssserver -c " + SHADOWSOCKS_CONFIG + " -d start")

    os.system("wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh")
    os.system("chmod +x bbr.sh")
    os.system("./bbr.sh")


config_system()


