import random
import string


def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    password = ([random.choice(letters.upper()) for l in range(2)] +
                [random.choice(digits) for d in range(1)] + [random.choice(special_chars) for s in range(1)])
    while len(password) < 10:
        password.append(random.choice(letters + digits + special_chars))
        print(password)
    random.shuffle(password)
    print(password)
    return ''.join(password)


print(generate_password())
