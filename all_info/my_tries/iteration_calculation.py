def iterator():
    while True:
        try:
            print("enter any positive number or print exit")
            operation = input()
            count = 0
            if operation == "exit":
                break
            elif operation.isdigit():
                # print("number is correct")
                length_of_number = len(operation)
                print("length", length_of_number)
                while length_of_number > 1:
                    operation = str(sum(map(int, operation)))
                    print(operation)
                    count += 1
                    length_of_number = len(operation)
                print("iteration count =", count)
        except Exception as e:
            print("Ошибка:", e)


iterator()
