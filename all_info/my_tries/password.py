import string
import secrets
alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (sum(c.isupper() for c in password) >= 2
            and sum(c.isdigit() for c in password) >= 1
            and sum(not c.isalnum() for c in password) >= 1):
        print(password)
        break
