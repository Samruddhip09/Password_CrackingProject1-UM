import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Test
print(hash_password("admin123"))
