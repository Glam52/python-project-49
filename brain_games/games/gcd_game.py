from random import randint
from brain_games.core import game_core


def game_generator() -> tuple:
    question = [randint(1, 100), randint(1, 100)]
    a = question[0]
    b = question[1]

    # finding the gcd
    while b:
        a, b = b, a % b
    answer = a

    question = ' '.join(str(x) for x in question)

    return question, answer


description = 'Find the greatest common divisor of given numbers.'

game_core(game_generator, description)
