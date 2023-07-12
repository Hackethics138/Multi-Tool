import requests
def track_ip_address(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'success':
        print("IP: ", data['query'])
        print("Country: ", data['country'])
        print("Region: ", data['regionName'])
        print("City: ", data['city'])
        print("ISP: ", data['isp'])
    else:
        print("Failed to track IP address.")


ip_address = input("Enter your ip:") 
track_ip_address(ip_address)
