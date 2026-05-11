from hashing import hash_password
from strength import check_strength

password = input("Enter password: ")

print("Hash:", hash_password(password))
print("Strength:", check_strength(password))