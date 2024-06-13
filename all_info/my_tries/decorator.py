import time
import string
import secrets


def outer():
    def inner():
        start_time = time.time()
        print(start_time)
        print("function execution")
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(10))
            if (sum(c.isupper() for c in password) >= 2
                    and sum(c.isdigit() for c in password) >= 1
                    and sum(not c.isalnum() for c in password) >= 1):
                print(password)
                time.sleep(5)
                break
        end_time = time.time()
        print(end_time)
        res_time = end_time - start_time
        res_time = round(res_time, 5)
        print(res_time)
        return res_time

    return inner()


outer()

