import random

def data_c():
    condition = int(input("Текущее состояние:\n"
                      "1. Усталый\n"
                      "2. Бодрый\n"))
    return(condition)

def data_i():
    inp = int(input("Входной сигнал:\n"
                  "1. Заказали 1 блюдо\n"
                  "2. Заказали 3 блюда\n"
                  "3. Заказали 5 блюд\n"))
    return(inp)

def rand ():
    rand_ver = random.uniform(0, 1)
    print(rand_ver)
    return rand_ver

def model(condition, input, output):
    if condition == 1 and inp == 1:
        for i in range (len(tired_1)):
            if rand_ver <= tired_1[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

    if condition == 1 and inp == 2:
        for i in range (len(tired_3)):
            if rand_ver <= tired_3[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

    if condition == 1 and inp == 3:
        for i in range (len(tired_5)):
            if rand_ver <= tired_5[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

    if condition == 2 and inp == 1:
        for i in range (len(cheerful_1)):
            if rand_ver <= cheerful_1[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

    if condition == 2 and inp == 2:
        for i in range (len(cheerful_3)):
            if rand_ver <= cheerful_3[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

    if condition == 2 and inp == 3:
        for i in range (len(cheerful_5)):
            if rand_ver <= cheerful_5[i]:
                print("Состояние", condition_m[i])
                print("Реакция на сигнал", output[i])
                break

if __name__ == '__main__':
    tired_1 = [0.39, 0.97, 0.98, 1]
    tired_3 = [0.28, 0.94, 0.96, 1]
    tired_5 = [0.19, 0.96, 0.97, 1]
    cheerful_1 = [0.02, 0.12, 0.99, 1]
    cheerful_3 = [0.05, 0.07, 0.82, 1]
    cheerful_5 = [0.07, 0.1, 0.73, 1]

    condition_m = ["Усталый", "Усталый", "Бодрый", "Бодрый"]
    output = ["Запомнил", "Забыл", "Запомнил", "Забыл"]
    signal = ["Заказали 1 блюдо", "Заказали 3 блюда", "Заказали 5 блюд"]

    rand_ver = rand()
    condition = data_c()
    inp = data_i()
    print()
    model(condition, inp, output)