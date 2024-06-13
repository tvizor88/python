def decorator_func(func):
    def wrapper():
        print("something")
        func()
        print("something else")
    return wrapper


def hello():
    print("hello")


if __name__ == "__main__":
    speech = decorator_func(hello)
    speech()
    hello()
