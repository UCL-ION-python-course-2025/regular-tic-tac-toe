# Wild Tic-Tac-Toe :o::x::x::x::o:

Wild Tic-Tac-Toe is a twist on the classic game of Tic-Tac-Toe.

![Wild Tic-Tac-Toe. Player 1 = blue. Player 2 = red](images/wildttt.jpeg)

## Rules of Wild Tic-Tac-Toe :o:

Like normal Tic-Tac-Toe, both players attempt to play 3 of the same counter (`O` or `X`) in a row on a **3 x 3** grid.

**The twist is that both players can choose to play an `O` or a `X`** on any move. The winner is whoever plays the **3rd `X` or `O` in a line** (horizontally, vertically or diagonally) of `X`'s or `O`'s.

![Wild Tic-Tac-Toe win. Blue has won here (since blue played last & completed the line of 3)](images/wild_ttt_win.jpeg)

In the image above, you can see a win for blue (player 1) resulting from 3 `X`'s, 2 of which were played by blue and 1 by red (player 2). Player 1 goes first, so has placed the winning counter here.

![Wild Tic-Tac-Toe game in progress. Red to play next.](images/wild_ttt_ongoing.jpeg)

In this image, you can see an ongoing game. You are player 2, playing the red counters. There are `12` possible moves you could make, since you can place an `X` or an `O` on any empty space.

Think about why it may be wise to play an `O` here!

Your task is to write code that plays **Wild Tic-Tac-Toe**.

## Human player

You will be playing against your own bot in this game! Click on the board to take a move. Left click to place an `O`. Right click to place an `X`.

If you cannot see the board when you click run, click the "+" button next to the Console. Then open "VNC". You should see the board in this tab.

If you'd rather your bot played against a random opponent without the visuals, change the bottom line of main.py to this:

```python
play_wild_ttt_game(
     your_choose_move=choose_move,
     opponent_choose_move=choose_move_randomly,
     game_speed_multiplier=1,
     verbose=True,
     render=False,
 )
```

## Competition Rules :scroll:

-   You can only write code in the `choose_move` function in `main.py`.
   - In the competition, your agent will call the `choose_move()` function in `main.py` to select a move
   - Any code not in `main.py` **will not be used**.


## Technical Details :hammer:

### New concepts

There are a few new python concepts you will need for this exercise (and to understand the example in `choose_move()`). These are detailed in `python_concepts.md`

### The **`choose_move()`** Function

In the competition, the **`choose_move()`** function is called to make your next move.

**Inputs:**

1. The board - a flat list of strings `" "` for empty, `"X"` or `"O"`, where the grid below shows how the list index corresponds to locations on the board. E.g. top left corner is the first element of the list.

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

E.g. `["O", " ", " ", "O", " ", "X", " ", " ", "X"]` represents:

```
O |   |
O |   | X
  |   | X
```



### Example in your `choose_move` function

We have provided (commented out) example that moves randomly. This could be a good guide on how to start building your solution.


## Competition Format :crossed_swords:

The competition will consist of your AI playing other teams' AIs 1-v-1 in a knockout tournament fashion.

Since going first gives an advantage, each 1-v-1 matchup consists of a **pair of games**. Each player starts one of the 2 games. In the event of a tie, it will go to a **sudden-death duel** :skull: (tiebreaker games). These 'duels' will be pairs of games with 1 player starting each game.


![Example knockout tournament tree](./images/tournament_tree.png)