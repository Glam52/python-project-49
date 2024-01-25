from random import randint
from typing import Tuple, List
from brain_games.launcher import launch_game


def game_generator() -> Tuple[List[str], str]:

    """
    This function creates a progression of random numbers,
    creates a gap in one of the numbers and remembers the missing number
    @rtype: Tuple
    @return: question for the user and a ready answer for comparison
    """

    start_progress = randint(1, 50)
    step_progress = randint(1, 5)
    empty_step = randint(0, 9)

    progression = list(map(lambda i: str(start_progress + i * step_progress),
                           range(10))
                       )

    progression[empty_step], answer = "..", str(progression[empty_step])
    question = ' '.join(progression)

    return question, answer


DESCRIPTION: str = 'What number is missing in the progression?'


def play():
    """
    This function is responsible for launching
    the game from the script
    """
    launch_game(game_generator, DESCRIPTION)
