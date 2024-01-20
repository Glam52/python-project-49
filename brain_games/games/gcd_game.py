from random import randint
from brain_games.core import game_core
from typing import Tuple, Callable


def game_generator() -> Tuple[str, str]:

    """
    This function generates 2 numbers and searches
    for their greatest common divisor
    @rtype: Tuple
    @return: question for the user and a ready answer for comparison
    """

    a = randint(1, 99)
    b = randint(1, 99)
    b_quest = b  # для помещения в генератор вопроса

    # finding the gcd
    while b:
        a, b = b, a % b
    answer = str(a)

    question = f'{a} {b_quest}'

    return question, answer


DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'

game_core(game_generator, DESCRIPTION)


def play() -> Callable:
    """
    this function helps to run the game from the script
    """

    game_core(game_generator, DESCRIPTION)
