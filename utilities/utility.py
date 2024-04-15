import string
import random


def generate_random_name(length):
    characters = string.ascii_lowercase
    sb = ''.join(random.choice(characters) for _ in range(length))
    return sb


def generate_random_password(length):
    characters = string.ascii_lowercase
    sb = ''.join(random.choice(characters) for _ in range(length))
    return sb


def generate_random_email(length):
    characters = string.ascii_lowercase
    sb = ''.join(random.choice(characters) for _ in range(length))
    sb.endswith("@mail.com")
    return sb


def generate_random_not_valid_email(length):
    characters = string.ascii_lowercase
    sb = ''.join(random.choice(characters) for _ in range(length))
    sb.endswith("dummy")
    return sb


def generate_random_phone_number(length):
    sb = ''
    random_generator = random.SystemRandom()
    for i in range(length):
        sb += str(random_generator.randint(0, 9))
    return sb










