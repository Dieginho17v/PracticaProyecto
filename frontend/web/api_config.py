import requests

API_BASE = "http://127.0.0.1:5000"

def api_get(path):
    return requests.get(API_BASE + path).json()

def api_post(path, data):
    return requests.post(API_BASE + path, json=data).json()

def api_put(path, data):
    return requests.put(API_BASE + path, json=data).json()

def api_delete(path):
    return requests.delete(API_BASE + path).json()