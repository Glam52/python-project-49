import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def question():
    pass


def decision():
    pass


# Основной движок игры
def main_cicle(question, correct_answer="correct_answer", name='NAME', condition='condition'):
    print(f'{condition}')

    count = 0
    for _ in range(3):
        question()

        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {name}")
            break
        else:
            print('Correct!')

    if count == 3:
        print(f'Congratulations, {name}')

