from random import randint, choice
from brain_games.core import game_core


# The basic logic of the game
def game_generator() -> tuple:
    operator = ['+', '-', '*']
    question = [randint(1, 99), choice(operator), randint(1, 99)]
    if question[1] == '+':
        answer = question[0] + question[2]
    elif question[1] == '-':
        answer = question[0] - question[2]
    elif question[1] == '*':
        answer = question[0] * question[2]

    question = ' '.join(str(x) for x in question)
    return question, answer


'''
This function generates a random expression and returns its answer
:var question: a random expression, a string with 2 numbers and an operator
:var answer: a string with an answer number
'''


description = 'What is the result of the expression?'

game_core(game_generator, description)
