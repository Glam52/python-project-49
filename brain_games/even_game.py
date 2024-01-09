from random import randint

import prompt


# Функция проверки на четность
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def even():
    # Строка с правилами игры
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0  # счетчик ответов

    # основной цикл игры
    for _ in range(3):
        rand_x = randint(1, 999)  # новое число для пользователя
        print('Question:', rand_x)

        answer = input('Your answer: ')  # получаем ответ пользователя
        if answer == 'yes':
            x = True
        elif answer == 'no':
            x = False
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was..")
            break

        # сравниваем ответ и функцию-проверку
        if is_even(rand_x) != x:
            if x == True:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                      f"Let's try again")
            elif x == False:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                      f"Let's try again")
            break
        elif is_even(rand_x) == x:
            print('Correct!')
            count += 1

    if count == 3:
        print('Congratulations')


even()


