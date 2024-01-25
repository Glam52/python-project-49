from brain_games.games.gcd_game import game_generator, DESCRIPTION
from brain_games.launcher import launch_game


def main():
    launch_game(game_generator, DESCRIPTION)


if __name__ == '__main__':
    main()
