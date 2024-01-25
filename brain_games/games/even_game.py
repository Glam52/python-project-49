from random import randint
from typing import Tuple
from brain_games.launcher import launch_game


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


def play():
    """
    This function is responsible for launching
    the game from the script
    """
    launch_game(game_generator, DESCRIPTION)
