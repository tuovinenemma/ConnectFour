# Implementation Document

Connect Four game using Pygame library in Python. The game features an AI opponent that utilizes the Minimax algorithm for searching the game tree and finding the best move. Alpha Beta pruning is used to boost the performance of the Minimax algorithm.


## Structure of the program
The program has beenn divided to four different files:

    * board.py creates the base for the game.
    * gameloop.py focuces on the logic of the connect four game.
    * minimax.py has the ai of the game including minimax and alpha beta pruning
    * screen.py focuces on the games GUI.


## Implementation of AI

The game AI implementation employs the minimax algorithm and alpha-beta pruning. The AI class takes the current game board state as an object and the depth of calculation (i.e., the number of moves ahead to evaluate) as parameters. The method applies the minimax algorithm, which uses alpha-beta pruning, to recursively traverse the game tree up to the specified depth and returns the best-scored column.

Without alpha-beta pruning, the minimax algorithm would examine every node in the game tree, and the number of nodes grows exponentially as the depth increases. Therefore, to ensure algorithmic efficiency, the depth limit when using the minimax algorithm alone should not exceed 3. Alpha-beta pruning reduced the size of the game tree traversed, significantly improving the algorithm's processing time. With the latest optimizations, the depth limit was increased to 5, a considerable improvement from before.


## Time & Space Complexity

The time complexity of the above implementation of the minimax algorithm depends on the search depth, which in this implementation was set to a maximum of 5. The branching factor, i.e., the number of possible moves in a game turn, starts at 7 in the beginning of the game and decreases as columns get filled up. In the worst case scenario, when no pruning occurs and all branches are explored, the time complexity of the algorithm is O(b^d), where b is the branching factor and d is the depth of the search tree. However, with the implemented alpha-beta pruning, the branching factor remains the same, but the search tree gets pruned to some extent by not exploring every branch. With minimax and alpha beta pruningthe time complexity is O(n).

## Graphical user interface

The program's graphical user interface was developed using Pygame, which utilizes straightforward mouse clicking to detect movements.

![Screenshot from 2023-03-15 12-04-22](https://user-images.githubusercontent.com/102189885/225276993-eb6e1292-6b4b-4bc5-a945-55641e3e87c2.png)

## What can be improved:
* The game would offer various levels with differing difficulty settings. Depending on the level you choose, the depth of the Minimax algorithm will be adjusted accordingly.
* Incorporating a more intricate graphical user interface would enhance the overall gameplay experience, resulting in increased enjoyment for the player.

## Sources

* https://en.wikipedia.org/wiki/Minimax
* https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
* https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
