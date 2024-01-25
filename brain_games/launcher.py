from brain_games.core import game_core
from typing import Callable, Any


def launch_game(game_generator: Callable[..., Any],
                DESCRIPTION: str):
    """
    This function starts the game
    @param game_generator: callable from game module
    @param DESCRIPTION: string from game module
    @rtype: None
    """
    game_core(game_generator, DESCRIPTION)
