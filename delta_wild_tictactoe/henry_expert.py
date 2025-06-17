import random
from typing import Dict, List, Tuple

from tqdm import tqdm

from game_mechanics import Cell, WildTictactoeEnv, load_dictionary, render, save_dictionary, Player

TEAM_NAME = "Henry"  # <---- Enter your team name here!


def train(game) -> Dict:
    """Write this function to train your algorithm! DOCSTRING NEEDS SOME TLC AND MOST WILL BE IN
    README.md.

    Arg:
        game:
            The environment that you will interact with to play wild tictactoe.
            The game environment has two functions you will need to call, step and reset.

    Functions:
        reset: starts a new game with a clean board, randomly choose the player
               to go first.
        step:  Make a move on the current board. This function takes three arguments:
               position & counter (see choose_move for more details) and verbose - whether
               to print the state of the board after each move.

    Variables:
        Both reset and step return the same 4 variables --
        observation (List[int]): The state of the board as a list of ints (see choose_move)
        reward [1, 0 or None]: The reward from the environment after the current move.
                               1 = win, 0 = draw/lose, None = no winner on this turn
        done (bool): True if the game is over, False otherwise.
        info (dict): Additional information about the current state of the game.
                     "winner": the winner of the game, if there is one.
                     "player_move": the player who just moved.

    Returns:
        A dictionary containing data to be used by your agent during gameplay.
        You can structure this however you like as long as you write a
        choose_move function that can use it.
    """
    # Set hyperparameters
    alpha = 0.25
    alpha_decay = 0.9999
    epsilon = 0.3
    # This is the default value of each state (the value at initialisation)
    default = 0

    # Initialise empty value function
    value_fn = {}

    # Train for 100,000 episodes
    for _ in tqdm(range(10_000)):

        state, reward, done, info = game.reset()

        while not done:
            # Use epsilon-greedy to take moves
            if random.random() < epsilon:
                action = choose_randomly(state)
            else:
                action = choose_move(state, value_fn)
            prev_state = state

            state, reward, done, info = game.step(action[0], action[1], verbose=False)
            reward = reward or 0

            # The alpha * (r_t + v(s_t+1)) term is negative because players alternate
            value_fn[str(prev_state)] = (1 - alpha) * value_fn.get(
                str(prev_state), default
            ) - alpha * (reward + value_fn.get(str(state), default))

        value_fn[str(state)] = reward
        # We decay alpha so we take smaller and smaller steps updating the policy as we converge
        #  to the optimal policy & value function
        alpha *= alpha_decay

    validate_value_fn(WildTictactoeEnv(), value_fn)

    return value_fn


def choose_move(board: List, value_function: Dict) -> Tuple[int, Cell]:
    """This function will be called during competitive play. It will take the current state of the
    board. You will need to return a single move to play on this board.

    Args:
        board: list representing the board.

            Elements which are 0 are empty spaces.
            Elements which are 1 are YOUR crosses.
            Elements which are -1 are THE OPPONENT's noughts.

        Example input: [0, 0, 1, -1, 0, 1, -1, 0, 0]
            Where above represents:

                |   | X
             -----------
              O |   | X
             -----------
              O |   |

        value_function: The dictionary you saved in your training function.

    Returns:
        position (int): The position you want to place your piece in (an integer 0 -> 8),
                        where 0 is the top left square and 8 is the bottom right.
        counter (Cell): The counter you want to use to place your piece. Either Cell.X or Cell.O.

    """
    poss_positions: List[int] = [count for count, item in enumerate(board) if item == Cell.EMPTY]
    counters: List[Cell] = [Cell.O, Cell.X]

    # Below picks randomly between highest value successor states
    max_value = -1000
    best_moves = []
    for pos in poss_positions:
        for counter in counters:
            # .copy() stops the changes we make from affecting the actual board
            state = board.copy()
            state[pos] = counter
            value = value_function.get(str(state), 0)
            if value > max_value:
                max_value = value
                best_moves = [(pos, counter)]
            elif value == max_value:
                best_moves.append((pos, counter))
    return random.choice(best_moves)


def choose_randomly(board: List[str]):
    position: int = random.choice([count for count, item in enumerate(board) if item == Cell.EMPTY])
    counter: str = random.choice([Cell.O, Cell.X])
    return position, counter


def validate_value_fn(game, my_dict: Dict):
    """Test your algorithm here!

    Args:
        game: a new instance of the wild tictactoe environment, as above.
        my_dict (Dict): the dictionary you returned from your training function.

    The example below plays a single game of wild tictactoe against itself, think about
    how you might want to adapt this to test the performance of your algorithm.
    """
    for oppo in [("Random", choose_randomly), ("Yourself", lambda x: choose_move(x, my_dict))]:
        num_won, num_drawn, num_lost = 0, 0, 0
        for _ in range(1000):
            observation, reward, done, info = game.reset()
            states = []
            while not done:
                if game.player_move == Player.Player1:
                    next_position, next_counter = choose_move(observation, my_dict)
                else:
                    next_position, next_counter = oppo[1](observation)
                observation, reward, done, info = game.step(
                    next_position, next_counter, verbose=False
                )
                states.append(
                    (
                        Player.Player1 if game.player_move == Player.Player2 else Player.Player2,
                        str(game),
                    )
                )

            if info["winner"] is None:
                num_drawn += 1
            elif game.player_move == Player.Player2:
                num_won += 1
            else:
                num_lost += 1
        print(f"Vs {oppo[0]}.\nWon: {num_won}, drawn: {num_drawn}, lost: {num_lost}")


if __name__ == "__main__":

    value_fn = train(WildTictactoeEnv())
    save_dictionary(value_fn, TEAM_NAME)
    value_fn = load_dictionary(TEAM_NAME)
    validate_value_fn(WildTictactoeEnv(), value_fn)
    render(choose_move, value_fn)
