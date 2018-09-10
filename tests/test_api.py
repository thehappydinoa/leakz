import hashlib

import pytest

import leakz

email = "not_a_real_email_123@github.io"
password = "derrick09"


def test_leaked_mail() -> None:
    with pytest.raises(leakz.LeakzNotLeaked):
        leakz.leaked_mail(email)


def test_password_from_hash() -> None:
    response = leakz.password_from_hash("e6e7c0a347468dd5cc73712fa53861cb")
    assert isinstance(response, str)
    assert response == password


def test_hashes_from_password() -> None:
    response = leakz.hashes_from_password(password)
    assert response.get("md5") == hashlib.md5(password.encode()).hexdigest()
    assert response.get("sha1") == hashlib.sha1(password.encode()).hexdigest()
    assert response.get("sha224") == hashlib.sha224(password.encode()).hexdigest()
    assert response.get("sha256") == hashlib.sha256(password.encode()).hexdigest()
    assert response.get("sha384") == hashlib.sha384(password.encode()).hexdigest()
    assert response.get("sha512") == hashlib.sha512(password.encode()).hexdigest()
