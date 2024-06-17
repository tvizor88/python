import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем начальное время
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Запоминаем конечное время
        time_taken = end_time - start_time  # Вычисляем затраченное время
        print(f"Функция {func.__name__!r} выполнилась за {round(time_taken, 3)} сек.")  # Печатаем имя функции и время, округленное до миллисекунд
        return result
    return wrapper


# Пример использования декоратора @timeit
@timeit
def example_function():
    for _ in range(1000000):
        pass  # Просто заглушка для цикла


example_function()
