import prompt
from typing import Callable, Tuple


def game_core(game_generator: Callable[[], Tuple[str, str]],
              description: str
              ):

    """
    This function is the main engine of the game,
    only the logic of the generator changes
    @param: A Callable generating a question and answer
    @param: description: It is a description of the game to the user
    """

    # General greeting in the game
    name = prompt.string('May I have your name? ')

    # Description of the game
    print(f"Hello, {name} \n "
          f"{description}")

    # Question/answer loop
    count = 0
    for _ in range(3):
        question, corect_answer = game_generator()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ').lower()

        if str(corect_answer) != str(user_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{corect_answer}' \n"
                  f"Let's try again, {name}!")
            break

        else:
            print('Correct')
            count += 1

    if count == 3:
        return print(f"Congratulations, {name}!")
