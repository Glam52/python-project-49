from random import randint
from brain_games.core import game_core
from typing import Tuple


def game_generator() -> Tuple[str, str]:
    a = randint(1, 99)
    b = randint(1, 99)
    b_quest = b # для помещения в генератор вопроса

    # finding the gcd
    while b:
        a, b = b, a % b
    answer = str(a)

    question = f'{a} {b_quest}'

    return question, answer


'''
This function generates 2 numbers and searches for their greatest common divisor
:var question: a string of two numbers
:var answer: a string of one number, the result of the calculation
'''

description = 'Find the greatest common divisor of given numbers.'

game_core(game_generator, description)
