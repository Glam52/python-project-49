def game_core(game_generator: tuple,
              description: str
              ) -> str:

    '''
    This function is the main engine of the game,
    only the logic of the generator changes
    :param game_generator: A tuple generating a question and answer
    :param description: It is a description of the game to the user
    '''

    # General greeting in the game
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f'Hello, {name}')

    # Description of the game
    print(description)

    # Question/answer loop
    count = 0
    for _ in range(3):
        question, corect_answer = game_generator()

        print(f'Question: {question}')

        user_answer = input('Your answer: ').lower()

        if str(corect_answer) != str(user_answer):
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {corect_answer} \n'
                  f"Let's try again, {name}")
            break

        else:
            print('Correct')
            count += 1

    if count == 3:
        print(f"Congratulations, {name}!")
