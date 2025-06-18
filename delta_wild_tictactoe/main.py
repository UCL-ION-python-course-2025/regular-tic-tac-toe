import random

from game_mechanics import (
    human_player,
    play_ttt_game,
)

TEAM_NAME = "Team Name"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"


def choose_move(board):
    """
    This is what will be called during competitive play.
    It takes the current state of the board as input.
    It returns a single move to play.

    Input:
        board: list representing the board.
               (see README Technical Details for more info)

    Returns:
        position (int): The position to place your piece
                        (an integer 0 -> 8), where 0 is
                        top left and 8 is bottom right.
    """

    # We provide an example here that chooses a random position on the board and
    # and places a random counter there.
    # See python_concepts.md if you don't understand this.
    # empty_positions = []
    # for idx in range(9):
    #     if board[idx] == " ":
    #         empty_positions.append(idx)
    # return random.choice(empty_positions)

    raise NotImplementedError("You need to implement this function!")


if __name__ == "__main__":

    # Play against your bot!!
    play_ttt_game(
        your_choose_move=human_player,
        opponent_choose_move=choose_move,
        game_speed_multiplier=10,
        verbose=True,
        render=True,
    )
