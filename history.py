from random import random, choice, randrange
from time import sleep

wait_time = randrange(1, 5)
nol = 2 #randrange(2)
sleep(3)
print("Привет")
sleep(2)
user_name = input("как тебя зовут?\n")# TODO сократить имя, если оно длиннее 25 символов(1 ч, 20 мин)
u = len(user_name)
print("ваше имя длинной "+str(u)+" символов")
incorrect_name = True
while incorrect_name == True:
    if u == 0:
        user_name = input("впишите свое имя\n")
        u = len(user_name)
    if u > 25:
        user_name = input("Имя слишком длинное, сократите(не более 25 символов)\n")
        u = len(user_name)
    if u > 0 and u < 25:
        incorrect_name = False
                    # TODO запретить пустой ввод(25 мин)
for s in range(nol):
                                    # TODO вопрос должен включать в себя больше 3 символов(1 ч)
    question = input(user_name+" задай вопрос\n")
    q = len(question)
    print("ваш вопрос длинной "+str(q)+" символов")
    if q<3:
        print("это не вопрос")
    else:
        print(end="мой ответ")
        for i in range(wait_time):
            print(".", end='')
            sleep(1)
        answer = choice(["да", "нет", "мне лень отвечать", "не могу дать ответ", "отстань:D"])
        print(answer)
# TODO 3 вопроса на 2-ой всегда "да"
