from brain_games.games.calc_game import game_generator, DESCRIPTION
from brain_games.core import game_core


def main():
    game_core(game_generator, DESCRIPTION)


if __name__ == '__main__':
    main()
