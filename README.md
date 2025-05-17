# Conway’s Game of Life – Interactive Visualiser

This is a Python implementation of Conway’s Game of Life using Pygame.

## 📦 Features

- Interactive cell simulation with visual grid
- Load/save patterns (`patterns.txt`)
- Real-time FPS and live cell counter
- Control the simulation with keyboard shortcuts

## 🛠 Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```

## 🚀 Run the Program

```bash
python life.py --width 40 --height 20 --fps 6
```

## 🎮 Controls

| Key      | Action                  |
|----------|-------------------------|
| `Space`  | Play / Pause            |
| `N`      | Step one generation     |
| `R`      | Random pattern          |
| `C`      | Clear the grid          |
| `S`      | Save current pattern    |
| `L`      | Load pattern from file  |

## 🧪 Sample Pattern

Create a `patterns.txt` file in the same folder with this content:

```
# Pattern: Glider
1,0
2,1
0,2
1,2
2,2
```

Press `L` to load this pattern.

## 🧬 Rules of Life

- Fewer than 2 neighbours → dies (underpopulation)
- 2 or 3 neighbours → lives on
- More than 3 neighbours → dies (overpopulation)
- Exactly 3 neighbours and dead → becomes alive

Enjoy exploring cellular automata!
