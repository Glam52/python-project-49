from random import randint
from brain_games.core import game_core


def game_generator():
    question = []
    start_progress = randint(1, 50)
    step_progress = randint(1, 5)
    empty_step = randint(0, 9)

    for i in range(10):
        if i == empty_step:
            question.append('...')
            start_progress += step_progress
            answer = start_progress + step_progress
        else:
            start_progress += step_progress
            question.append(start_progress + step_progress)

    question = ' '.join(str(x) for x in question)

    return question, answer


description = 'What number is missing in the progression?'

game_core(game_generator, description)
