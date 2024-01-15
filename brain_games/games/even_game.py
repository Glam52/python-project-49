from random import randint
from brain_games.core import game_core


def game_generator():
    question = [randint(1, 99)]
    if question[0] % 2 == 0:
        answer = ['yes']
    else:
        answer = ['no']

    question = " ".join(str(x) for x in question)
    answer = " ".join(str(x) for x in answer)

    return question, answer


description = 'Answer "yes" if the number is even, otherwise answer "no".'

game_core(game_generator, description)
