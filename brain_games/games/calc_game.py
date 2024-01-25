from random import randint, choice
from typing import Tuple
from brain_games.launcher import launch_game


# The basic logic of the game
def game_generator() -> Tuple[str, str]:

    """
    This function generates a random mathematical operation
    and returns the answer to it
    @rtype: Tuple
    @return: question for the user and a ready answer for comparison
    """

    operator = choice(['+', '-', '*'])
    first_dig = randint(1, 99)
    last_dig = randint(1, 99)

    if operator == '+':
        answer = str(first_dig + last_dig)
    elif operator == '-':
        answer = str(first_dig - last_dig)
    elif operator == '*':
        answer = str(first_dig * last_dig)

    question = f'{first_dig} {operator} {last_dig}'
    return question, answer


DESCRIPTION: str = 'What is the result of the expression?'


def play():
    """
    This function is responsible for launching
    the game from the script
    """
    launch_game(game_generator, DESCRIPTION)
