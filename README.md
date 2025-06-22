# 🏓 Pong Game (Python OOP)

This is a **2-player Pong Game** built using **Python** and the **Turtle graphics module**, structured with **Object-Oriented Programming (OOP)** principles. The game includes dynamic ball movement, player paddles, custom score targets, and real-time winner detection.

## 🚀 Features

- 🎮 Two-player interactive gameplay  
  - Player 1 uses `Arrow Up` and `Arrow Down` keys  
  - Player 2 uses `W` and `S` keys  
- 🔢 Custom player names and score target input at game start  
- 🏓 Ball bounces off top and bottom walls  
- 🛡 Ball reflects off paddles with increasing speed  
- ⚽ Score is updated when a player misses the ball  
- 🏆 Winner is displayed when target score is reached  

## 🧠 Class Overview

### `Paddle` (`paddle.py`)
- Creates paddle objects at given positions
- Handles vertical movement (up/down) within bounds

### `Ball` (`ball.py`)
- Manages automatic ball movement
- Handles bouncing off walls and paddles
- Resets position after a score

### `Scoreboard` (`scoreboard.py`)
- Displays current scores of both players
- Declares and displays the winner

### `main.py`
- Initializes screen, paddles, ball, and scoreboard
- Accepts player names and target score
- Contains main game loop and collision logic

## 🎮 Controls

- **Player 1:**  
  `↑` – Move Up  
  `↓` – Move Down

- **Player 2:**  
  `W` – Move Up  
  `S` – Move Down

## 📁 Project Structure

pong game
├── main.py<br>
├── paddle.py<br>
├── ball.py<br>
└── scoreboard.py 

## 🛠 Requirements

- Python 3.x  
- `turtle` module (comes with Python)

## ▶️ How to Run

1. Ensure all files are inside a folder named `snake game/`
2. Open a terminal or IDE in that directory
3. Run the game using:

