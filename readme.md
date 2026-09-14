#  Pixel Runner

A pixel-style endless runner game built using **Python and Pygame**.

The player controls a character who must jump over ground obstacles and avoid flying enemies while trying to survive for as long as possible and achieve the highest score.

The game is also available as a web version using **Pygbag**, allowing it to run directly inside a web browser.

---

## ✨ Features

-  Endless runner gameplay
-  Animated player character
-  Jump mechanics
-  Moving snail obstacles
-  Flying obstacles
-  Collision detection
-  Survival-based score system
-  Start and game-over screens
-  Sound effects
-  Game audio support
-  Keyboard controls
-  Mouse click jump support
-  Browser version using Pygbag

---

##  Gameplay

The objective of Pixel Runner is simple:

**Run → Jump → Avoid Obstacles → Survive → Get the Highest Score!**

The player automatically runs while obstacles move from the right side of the screen toward the player.

Jump over ground obstacles and avoid flying enemies.

If the player collides with an obstacle, the game ends and the final score is displayed.

---

##  Controls

| Control | Action |
|---|---|
| `SPACE` | Jump |
| `Mouse Click` | Jump |
| `Close Window` | Exit Game |

---

##  How It Was Made

Pixel Runner was developed using **Python and Pygame**.

The game uses a continuous game loop to handle:

- Player movement
- Gravity
- Jumping
- Sprite animation
- Obstacle movement
- Collision detection
- Score calculation
- Game states
- Sound effects

The game was converted into a browser-compatible version using **Pygbag**, allowing the Pygame application to run in a web browser.

---

##  Technologies Used

- Python
- Pygame
- Asyncio
- Pygbag
- WebAssembly
- HTML5

---

##  Project Structure

```text
pygame-runner/
│
├── audio/
│   └── Game sound files
│
├── build/
│   └── web/
│       └── Pygbag web build
│
├── font/
│   └── Pixel game font
│
├── graphics/
│   ├── player/
│   ├── snail/
│   ├── fly/
│   ├── Sky.png
│   └── ground.png
│
├── main.py
└── README.md

2. install The Game
pip install pygame

3. Run the game
python main.py

Author

chandu kumari

made as a fun project to learn python game development

repo link:https://github.com/rahulkumargupta0789-svg/pygame-runner

playable link:https://pygame-runner-6i88.vercel.app/