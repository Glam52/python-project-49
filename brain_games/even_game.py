from random import randint
from brain_games.greeting import welcome_user


name = welcome_user()


# Функция проверки на четность
def is_even(n: int) -> str:
    if n % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even():
    # Строка с правилами игры
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0  # счетчик ответов
    # основной цикл игры
    for _ in range(3):
        rand_x = randint(1, 999)  # новое число для пользователя
        print('Question:', rand_x)

        answer = input('Your answer: ')  # получаем ответ пользователя

        # сравниваем ответ и функцию-проверку
        if answer != is_even(rand_x):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{is_even(rand_x)}'\n"
                  f"Let's try again, {name}")
            break
        else:
            print('Correct!')
            count += 1

    if count == 3:
        print(f'Congratulations, {name}')
