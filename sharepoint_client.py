import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
SITE_NAME = "GraphTestSite"
TENANT = "yourtenant.sharepoint.com"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

url = f"https://graph.microsoft.com/v1.0/sites/{TENANT}:/sites/{SITE_NAME}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Site Details:")
    print(response.json())
else:
    print("Error:", response.text)
