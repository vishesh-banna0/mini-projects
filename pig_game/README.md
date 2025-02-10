# Pig Game

## Description
This is a simple multiplayer dice rolling game implemented in Python. The game supports 2 to 4 players, and the first player to reach or exceed a score of 50 wins.

## How to Play
1. The game prompts the user to enter the number of players (between 2 and 4).
2. Each player takes turns rolling a six-sided die.
3. Players can keep rolling to accumulate points or stop and add their current turn's points to their total score.
4. If a player rolls a 1, they lose all points earned during that turn, and their turn ends.
5. The first player to reach a score of 50 or more wins the game.

## Requirements
- Python 3.x

## How to Run
1. Copy the script into a Python file, e.g., `pig_game.py`.
2. Open a terminal or command prompt.
3. Run the script using:
   ```sh
   python pig_game.py
   ```
4. Follow the on-screen instructions to play the game.

## Code Explanation
- The `roll()` function generates a random number between 1 and 6.
- The game starts by asking the user for the number of players.
- Each player takes turns rolling the die and choosing whether to continue or end their turn.
- If a player rolls a 1, their turn ends and they lose any points accumulated in that round.
- The game continues until a player reaches or exceeds 50 points.

## Example Gameplay
```
Enter the Number of Players (2-4): 3
Player number 1 turn has just started!
Your total score is: 0
Would you like to roll (y)? y
You rolled a: 5
Your score is: 5
Would you like to roll (y)? y
You rolled a: 1
You rolled a 1! Turn done!
Your total score is: 0
...
Player number 2 is the winner with a score of: 50
```

## License
This project is open-source and free to use. Modify and enhance it as you like!

