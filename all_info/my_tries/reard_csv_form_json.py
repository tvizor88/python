with open('D:\python\project\python\lection_3\cars.csv', 'r', encoding='utf-8') as f:
    lines = 1
    print(f.readline())







    for line in f:
        print(lines)
        print(line)
        lines += 1
        for element in line:
            year = []
            make = []
            model = []
            if element == ",":
                print("element ,", element)
                year.append(element)
            else:
                print("element other", element)
                make.append(element)
        print("el odin", year)
        print("el dva", make)
