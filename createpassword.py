#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#generate new password
print("""
ONCE YOU PRESS ENTER, YOUR NEW PASSWORD WILL BE PRINTED OUT!
""")
main = input()

passwd = Fernet.generate_key()

print(passwd)

input("\n\n\n\n\npress ENTER when you are done")
