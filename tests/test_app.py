from app import Generator
import pytest


@pytest.fixture()
def password():
    generator = Generator()
    return generator.generate()

def test_check_generated_password_is_eight_charaters_long(password):
    assert len(password) == 8

def test_check_generated_password_has_2_uppercase(password):
    counter = 0
    for i in password:
        if i.isupper():
            counter += 1
    assert counter == 2

def test_check_generated_password_has_2_lowercase(password):
    counter = 0
    for i in password:
        if i.islower():
            counter += 1
    assert counter == 2

def test_check_generated_password_has_2_numbers(password):
    counter = 0
    for i in password:
        if i.isdigit():
            counter += 1
    assert counter == 2

def test_check_generated_password_has_2_special_characters(password):
    counter = 0
    for i in password:
        if not i.isalnum():
            counter += 1
    assert counter == 2