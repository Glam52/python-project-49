from random import randint, choice
from brain_games.greeting import welcome_user

name = welcome_user()


# логика калькулятора
def calc(first_dig: int, last_dig: int, operator: str) -> int:
    if operator == '+':
        return first_dig + last_dig
    elif operator == '-':
        return first_dig - last_dig
    elif operator == '*':
        return first_dig * last_dig


def game_calc():
    print('What is the result of the expression?')

    count = 0
    for _ in range(3):

        rand_a = randint(1, 99)
        rand_b = randint(1, 99)
        rand_oper = choice(['+', '-', '*'])

        print('Question:', rand_a, rand_oper, rand_b)

        answer = int(input('Your answer: '))

        if answer != calc(rand_a, rand_b, rand_oper):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{calc(rand_a, rand_b, rand_oper)}'\n"
                  f"Let's try again, {name}")
            break
        else:
            print('Correct!')
            count += 1

    if count == 3:
        print(f'Congratulations, {name}')

game_calc()
