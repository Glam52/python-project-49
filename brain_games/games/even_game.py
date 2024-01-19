from random import randint
from brain_games.core import game_core
from typing import Tuple


def game_generator() -> Tuple[str, str]:
    question = randint(1, 99)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return str(question), answer


'''
This function generates a random number and returns its even or odd
:var question: return string of one random number
:var answer: return string whether the number even or not.
'''


description = 'Answer "yes" if the number is even, otherwise answer "no".'

game_core(game_generator, description)
