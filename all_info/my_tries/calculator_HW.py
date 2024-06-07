def calculator():
    while True:
        print("""Введите первый операнд, математическое действие
         и второй операнд или 'exit' для выхода:""")
        operation = input()
        if operation == 'exit':
            break
        else:
            print("ok")
        formula = operation.split()
        if (len(formula) == 3 and formula[0].isdigit()
                and formula[2].isdigit() and
                formula[1] in ['+', '-', '*', '/']):
            num1 = int(formula[0])
            num2 = int(formula[2])
            operator = formula[1]
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                try:
                    result = num1 / num2
                except ZeroDivisionError:
                    print('Ошибка: Деление на ноль')
            print(f"Результат: {result}")
        else:
            print('Неправильная формула')


calculator()
