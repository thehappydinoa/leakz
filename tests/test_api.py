import leakz
import hashlib

email = "not_a_real_email_123@github.io"
password = "derrick09"

def test_leaked_mail():
    response = leakz.leaked_mail(email)
    assert isinstance(response, list)
    assert response == list()

def test_password_from_hash():
    response = leakz.password_from_hash("e6e7c0a347468dd5cc73712fa53861cb")
    assert isinstance(response, str)
    assert response == password

def test_hash_from_password():
    response = leakz.hash_from_password(password)
    assert response.get("md5") == hashlib.md5(password.encode()).hexdigest()
    assert response.get("sha1") == hashlib.sha1(password.encode()).hexdigest()
    assert response.get("sha224") == hashlib.sha224(password.encode()).hexdigest()
    assert response.get("sha256") == hashlib.sha256(password.encode()).hexdigest()
    assert response.get("sha384") == hashlib.sha384(password.encode()).hexdigest()
    assert response.get("sha512") == hashlib.sha512(password.encode()).hexdigest()