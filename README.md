# Rock-Paper-Scissors Terminal Game

A terminal-based Rock-Paper-Scissors game against the computer, with ASCII art, round scoring, and early-win detection.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [License](#license)

## Overview
This project implements a classic best-of-N Rock-Paper-Scissors match between the player and the computer, playable entirely from the command line.

## Features
- 🎯 Customizable number of rounds (best-of-N)
- 🎨 ASCII art for Rock, Paper, and Scissors
- 📊 Live round-by-round scoring
- 🏁 Automatic early termination once a winner is mathematically decided

## Installation
```bash
git clone https://github.com/Emmanuel-Fasina/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
```
No external dependencies — just Python 3.11+.

## Usage
```bash
python main.py
```
1. Enter the number of rounds you want to play.
2. For each round, choose `0` (Rock), `1` (Paper), or `2` (Scissors).
3. Results are shown after every round, with a final winner declared at the end (or early, if decided).

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

## How It Works
- The player picks `0`, `1`, or `2`; the computer picks randomly from the same set.
- Standard Rock-Paper-Scissors rules determine the round winner.
- The game ends early once one side has secured an unbeatable lead.

## Project Structure
```
Rock-Paper-Scissors/
├── main.py       # Game logic and CLI loop
└── README.md     # Project documentation
```

## Notes
- Invalid inputs (anything other than `0`, `1`, or `2`) are not currently handled — enter a valid option when prompted.

## License
This project was built for educational and learning purposes.

---
Built by [Emmanuel Fasina](https://github.com/Emmanuel-Fasina)
