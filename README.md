# Rock-Paper-Scissors

A simple Python terminal game that lets you play Rock-Paper-Scissors against the computer.

## Features

- Play a best-of series with a customizable number of rounds.
- Clear ASCII art for Rock, Paper, and Scissors.
- Round-by-round scoring and immediate win/lose detection.
- Early game termination when the match winner is decided before all rounds finish.

## How it works

- You choose one of three options:
  - `0` for Rock
  - `1` for Paper
  - `2` for Scissors
- The computer chooses randomly.
- The program compares both choices and prints the result.
- The first player to secure enough wins to make a comeback impossible ends the game early.

## Usage

1. Open a terminal and navigate to the project folder.
2. Run the game using Python:

```bash
python main.py
```

3. Enter the number of rounds you want to play.
4. For each round, type `0`, `1`, or `2` when asked.

## Example

```text
How many rounds do you want to play? 3
Round 1:
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: 0
You choose:
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Computer choose:
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You Win!
Your Wins: 1
Computer Wins: 0
```

## Requirements

- Python 3.11+

## Notes

- Invalid inputs are not currently handled by the script, so be sure to enter `0`, `1`, or `2` when prompted.
- The game is played entirely in the terminal.
