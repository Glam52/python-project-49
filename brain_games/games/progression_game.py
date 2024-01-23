from random import randint
from brain_games.core import game_core
from typing import Tuple, List, Callable


def game_generator() -> Tuple[List[int], str]:

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
    result = ' '.join(progression)

    return result, answer


DESCRIPTION: str = 'What number is missing in the progression?'
