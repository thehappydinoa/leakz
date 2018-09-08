import json

import requests


def api_request(path: str, base_url: str = "https://lea.kz") -> dict:
    try:
        return requests.get(base_url + path).json()
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return dict()


def leaked_mail(email_address: str) -> list:
    response = api_request("/api/mail/" + email_address).get("leaked")
    if response:
        return response.split(', ')
    return list()


def password_from_hash(hash: str) -> str:
    return api_request("/api/hash/" + hash).get("password")


def hash_from_password(password) -> dict:
    return api_request("/api/password/" + password)