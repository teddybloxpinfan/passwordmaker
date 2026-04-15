import os
from cryptography.fernet import Fernet

#generate new password
print("""
ONCE YOU PRESS ENTER, YOUR NEW PASSWORD WILL BE PRINTED OUT!
""")
main = input()

passwd = Fernet.generate_key()

print(passwd)
