from random import randint
import math
from brain_games.core import game_core


def game_generator() -> tuple:
    question = randint(1, 101)
    is_prime = True

    if question <= 1:
        answer = 'no'
    else:
        for i in range(2, math.isqrt(question) + 1):
            if question % i == 0:
                is_prime = False
                break

    if is_prime:
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer


'''
This function takes a random number and uses a formula
to determine whether it is simple
:var question: return the one number with which the action will be performed
:var answer: return string whether the number is prime or not
'''

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

game_core(game_generator, description)