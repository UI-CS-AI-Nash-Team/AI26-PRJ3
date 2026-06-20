# Othello AI - Adversarial Search

Implementation of intelligent agents for the Othello (Reversi) game using **Minimax** and **Alpha-Beta Pruning** algorithms.

## Project Description

This project was developed for the Artificial Intelligence course. The objective is to design an intelligent agent capable of playing Othello by searching the game tree and selecting the best possible move.

The game environment is provided by the course staff, while the following components are implemented in this project:

* Evaluation Function
* Minimax Search Agent
* Alpha-Beta Pruning Agent
* Performance Evaluation and Comparison

## Game Overview

Othello is a two-player board game played on a square board. Each player places pieces of their color (Black or White) on the board.

### Rules

* A move is valid only if it captures at least one opponent piece.
* Captured pieces change color.
* The game ends when neither player has a legal move.
* The winner is the player with more pieces on the board.

## Project Structure

```text
game/
├── othello.py

agents/
├── random_agent.py
├── greedy_agent.py
├── minimax_agent.py
└── alphabeta_agent.py

main.py
tournament.py
```

## Implemented Components

### 1. Evaluation Function

A heuristic evaluation function is used to estimate the quality of non-terminal game states.

Possible factors considered:

* Piece difference
* Mobility (number of legal moves)
* Corner occupancy
* Board control

### 2. Minimax Agent

The Minimax algorithm explores the game tree up to a specified depth and selects the move that maximizes the player's utility while assuming optimal play from the opponent.

### 3. Alpha-Beta Agent

Alpha-Beta pruning improves Minimax efficiency by eliminating branches that cannot affect the final decision.

Benefits:

* Fewer explored nodes
* Faster execution
* Same optimal decision as Minimax

## Running the Project

```bash
python main.py
```

or

```bash
python tournament.py
```

## Experiments

The implemented agents were evaluated against:

* Random Agent
* Greedy Agent

Each experiment was repeated multiple times to measure performance accurately.

### Sample Results

| Opponent     | Games | Wins | Win Rate |
| ------------ | ----- | ---- | -------- |
| Random Agent | 20    | 20   | 100%     |
| Greedy Agent | 20    | 15   | 75%      |


## Analysis

### Effect of Search Depth

Increasing search depth generally improves decision quality, but also increases computation time.

### Effect of Alpha-Beta Pruning

Alpha-Beta pruning significantly reduces the number of explored nodes and execution time while preserving the same decision quality as Minimax.

### Evaluation Function

The evaluation function combines several heuristics to estimate the strength of a board position.

### Limitations

* Limited search depth due to computational cost.
* Heuristic evaluation may not perfectly represent long-term strategic advantages.

## Technologies

* Python
* Minimax Algorithm
* Alpha-Beta Pruning
* Adversarial Search

## Course Information

**Course:** Artificial Intelligence
**Project:** Adversarial Search – Othello AI
**Semester:** 1404-1405

## Authors


* Hossein Karimjafari
* Erfan Moradi
* Sajad Mohammadi
* Behnam Moein

## Repository

> https://github.com/UI-CS-AI-Nash-Team/AI26-PRJ3
