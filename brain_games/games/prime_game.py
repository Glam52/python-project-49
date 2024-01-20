from random import randint
import math
from brain_games.core import game_core
from typing import Tuple


def game_generator() -> Tuple[str, str]:

    """
    This function takes a random number and uses a formula
    to determine whether it is simple
    @rtype: Tuple
    @return: question for the user and a ready answer for comparison
    """

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

    return str(question), answer


DESCRIPTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no".'

game_core(game_generator, DESCRIPTION)
