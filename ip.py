import requests
import webbrowser

def get_ip_info():
    response = requests.get("https://api.ipify.org?format=json")
    ip_info = response.json()
    return ip_info["ip"]

def open_google_maps(ip_address):
    google_maps_url = f"https://www.google.com/maps/@?api=1&query={ip_address}"
    webbrowser.open(google_maps_url)

def main():
    ip_address = get_ip_info()
    open_google_maps(ip_address)

if __name__ == "__main__":
    main()
