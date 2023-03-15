# Testing document

## Unit testing

The unit tests are executed using pytest and are located in the directory src/tests/. Running the unit tests can be accomplished in the project's root directory using the following command:
```
poetry run invoke test
```
Currently, the unit tests are verifying the functionality of several files: board.py, minimax, screen, and gameloop.

The unit tests test that the board is created correctly and different win scenarios.

## Test coverage
For getting the test coverage use command:
```
poetry run invoke coverage-report
```

![Screenshot from 2023-02-05 22-20-20](https://user-images.githubusercontent.com/102189885/216842782-ba6eb2f7-b634-4237-a3d4-188b7f979de4.png)

## Testing for gameboard
In unit testing of the game board, the objective is to verify the correctness of the Game, GameLoop and Screen classes methods that operate on the game board.

## Testing for AI
In unit testing of game AI, the aim is to verify the correctness of the AI class methods and the minimax algorithm. To test the accuracy of the AI, predetermined game situations are presented to it, where it is expected to choose a particular move. In some test scenarios, the correctness of the AI's move evaluation is also examined to ensure that it receives the appropriate score.
