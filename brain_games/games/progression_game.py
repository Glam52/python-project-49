from random import randint
from brain_games.core import game_core


def game_generator():
    start_progress = randint(1, 50)
    step_progress = randint(1, 5)
    empty_step = randint(0, 9)

    progression = list(map(lambda i: start_progress + i * step_progress, range(10)))

    progression[empty_step], answer = '..', str(progression[empty_step])

    return progression, answer


'''
This function creates a progression of random numbers,
creates a gap in one of the numbers and remembers the missing number
:var question: List of number progression with gap
:var answer: the missing number
'''


description = 'What number is missing in the progression?'

game_core(game_generator, description)
