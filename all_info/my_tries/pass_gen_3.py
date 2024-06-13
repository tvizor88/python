import string
import random


def generate_password():
    password = ([random.choice(string.ascii_letters.upper()) for l in range(2)] +
                [random.choice(string.digits) for d in range(1)] + [random.choice(string.punctuation) for s in range(1)])
    while len(password) < 10:
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        # print(password)
    random.shuffle(password)
    # print(password)
    return ''.join(password)


print(generate_password())
