import requests ip = requests.get("https://api.ipify.org").text print(f"Your IP 
is: {ip}") info = requests.get(f"http://ip-api.com/json/{ip}").json() 
print(f"Location: {info['city']}, {info['regionName']}")
print(f"ISP: {info['isp']}")
