import requests

from .exceptions import *

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


def api_request(path, base_url="https://lea.kz"):
    try:
        response = requests.get(base_url + path)
        if response.status_code == 404:
            raise LeakzNotLeaked
        return response.json()
    except requests.exceptions.RequestException:
        raise LeakzRequestException
    except JSONDecodeError:
        raise LeakzJSONDecodeException


def leaked_mail(email_address):
    response = api_request("/api/mail/" + email_address).get("leaked")
    if response:
        return response.split(', ')
    return list()


def password_from_hash(hash):
    return api_request("/api/hash/" + hash).get("password")


def hashes_from_password(password):
    return api_request("/api/password/" + password)
