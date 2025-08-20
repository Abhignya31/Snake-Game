# 🐍 Snake Game  

A modern **Snake Game built using Python and Pygame** with a clean login interface, difficulty modes, power-ups, and high score saving.  

---

## 🚀 Features  

- 🎮 **Login Screen** – Enter your name & choose difficulty (Easy, Medium, Hard)  
- 🖥️ **Full-Screen Gameplay** – Immersive snake game experience  
- ⚡ **Difficulty Levels** – Snake speed changes with difficulty  
- 🔵 **Power-Ups (Blue Food)** – Adds score & grows snake  
- 🔴 **Poison Food (Red Food)** – Reduces score & shrinks snake  
- 🏆 **High Scores** – Saves player scores in `scores.txt`  
- 💡 **Game Over Screen** – Replay or quit option  
- 🎨 **Logo + Background Support** – Can use `assets/logo.png`  

---


### 🔑 Login Screen  
👉 Enter name and difficulty  

### 🎮 Gameplay  
👉 Eat blue food to grow, avoid red poison food  

---

## 📂 Project Structure  
```text
Advanced-Snake-Game/
│── login1.py           # Login screen (name + difficulty selection)
│── main1.py            # Main snake game logic
│── scores.txt          # Stores all player scores
│── player.txt          # Stores last player session
│── assets/             # Store logo.png, background.png etc.
│── README.md           # Documentation
│── requirements.txt    # Dependencies (pygame)

```
---

## ⚡ Installation  

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/Advanced-Snake-Game.git
   cd Advanced-Snake-Game
   ```
## Install dependencies

```bash
pip install -r requirements.txt
```
## Run the game

```bash
python login1.py
```
## 🎮 Controls
⬅️ Left Arrow – Move Left

➡️ Right Arrow – Move Right

⬆️ Up Arrow – Move Up

⬇️ Down Arrow – Move Down

C – Replay after Game Over

Q – Quit after Game Over


## 🏆 High Scores
Scores are saved in scores.txt automatically after each game.

Example:
Abhignya, 50
Raj, 70
Guest, 30

---

## 📌 Future Enhancements

🔹 Obstacles (walls, moving blocks)

🔹 Special timed power-ups (double points, invincibility)

🔹 Background music and sound effects

🔹 Leaderboard UI to display top scores
