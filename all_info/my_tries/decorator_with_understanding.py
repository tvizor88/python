import time
import string
import random
from functools import wraps


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        full_time = end_time - start_time
        return result, full_time
    return wrapper


@execution_time
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    pas = ([random.choice(letters.upper()) for l in range(2)] +
           [random.choice(digits) for d in range(1)] + [random.choice(special_chars) for s in range(1)])
    while len(pas) < 10:
        pas.append(random.choice(letters + digits + special_chars))
    random.shuffle(pas)
    time.sleep(1.005)
    return ''.join(pas)


password, time_spent = generate_password()
print(f"Generated pass: {password}")
print("time spent for pass generation:", round(time_spent, 3))
