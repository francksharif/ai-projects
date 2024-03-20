import requests
from dotenv import load_dotenv
import os


load_dotenv()

key = os.getenv("HA_API_KEY")


def ha_file_analysis(file_data):
    url = 'https://www.hybrid-analysis.com/api/v2/quick-scan/file'
    headers = {'User-Agent': 'Falcon Sandbox', 'api-key': key}
    files = {'file': file_data}
    data = {'scan_type': 'all'}
    response = requests.post(url, headers=headers, files=files, data=data)
    return response.json()


def ha_file_report(id):
    url = f'https://www.hybrid-analysis.com/api/v2/quick-scan/{id}'
    headers = {'User-Agent': 'Falcon Sandbox', 'api-key': key}
    response = requests.get(url, headers=headers)
    return response.json()

