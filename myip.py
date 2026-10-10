import requests

print("My IP Tool - Only for educational purpose")

try:
    ip = requests.get("https://api.ipify.org").text
    print(f"Your IP: {ip}")

    target = input("Enter IP to get info: ")
    data = requests.get(f"http://ip-api.com/json/{target}").json()

    print("\n--- IP Info ---")
    print(f"IP: {data.get('query')}")
    print(f"Country: {data.get('country')}")
    print(f"City: {data.get('city')}")
    print(f"ISP: {data.get('isp')}")
    print(f"Timezone: {data.get('timezone')}")

except Exception as e:
    print(f"Error: {e}")
