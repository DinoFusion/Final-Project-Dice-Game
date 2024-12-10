# Dice Game

## Overview
This program simulates a simple dice game where players take turns rolling dice to score points. The objective is to reach a target score first.
The game includes data visualization to dynamically display player scores after each turn using the Seaborn library.

## Features
- Players take turns rolling three dice.
- "Tupled out" condition ends a turn with zero points.
- Matching dice are "fixed"; unfixed dice can be rerolled.
- Players can decide when to stop and score.
Data Visualization:
- A bar chart dynamically updates to show player scores after each turn.
-Visualization uses the Seaborn library for a clear and appealing display.

## Visualization
- After each player's turn, a bar chart displays the current scores of all players.
- The chart updates dynamically to reflect the latest scores.
  
## Data Analysis
- Scores from each turn are recorded in a Pandas DataFrame.
- After each round, the program provides a summary of:
- Total scores per player.
- Average (mean) scores per player.
- Maximum score achieved in a single turn for each player.
- A final summary is displayed at the end of the game.
