from random import randint, choice
from brain_games.core import game_core
from typing import Tuple


# The basic logic of the game
def game_generator() -> Tuple[str, str]:
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


'''
This function generates a random expression and returns its answer
:var question: a random expression, a string with 2 numbers and an operator
:var answer: a string with an answer number
'''


description = 'What is the result of the expression?'

game_core(game_generator, description)
