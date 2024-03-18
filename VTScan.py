import requests
from dotenv import load_dotenv
import os



load_dotenv()
key = os.getenv("VT_API_KEY")


def vt_file_analysis(file_data):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    files = {'file': file_data}
    params = {'apikey': key}
    response = requests.post(url, files=files, params=params)
    return response.json()


def vt_scan_report(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': key, 'resource': resource}
    response = requests.get(url, params=params)
    return response.json()