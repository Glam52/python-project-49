from random import randint
from brain_games.core import game_core
from typing import Tuple, Callable


def game_generator() -> Tuple[str, str]:
    """
    This function generates a random number and checks if it is even
    @rtype: Tuple
    @return: question for the user and a ready answer for comparison
    """

    question = randint(1, 99)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return str(question), answer


DESCRIPTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def play() -> Callable:

    """
    this function helps to run the game from the script
    """

    game_core(game_generator, DESCRIPTION)


# Запуск игры
play()
