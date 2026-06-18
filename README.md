# Snake Game 🐍

A classic Snake game built from scratch in Python using the built-in `turtle` module, with an object-oriented design.

## Features

- Smooth, controllable snake movement with arrow key controls
- Snake grows by one segment each time it eats food
- Live scoreboard that updates on every food pickup
- Game over on wall collision or self-collision
- Reverse-direction prevention (snake can't instantly turn back into itself)

## Project Structure

```
snake_game/
├── main.py          # Game loop, screen setup, collision checks
├── snake.py          # Snake class — movement, growth, direction control
├── food.py            # Food class — random placement on the board
├── scoreboard.py     # Scoreboard class — score tracking and game over message
└── README.md
```

Each part of the game is handled by its own class, which keeps the code organized and easy to extend:

- **`Snake`** owns a list of `Turtle` segments (composition over inheritance) so the body can grow dynamically.
- **`Food`** and **`Scoreboard`** each inherit directly from `Turtle`, since they're simple, single-shape entities.

## How to Run

```bash
python main.py
```

No external dependencies — this project only uses Python's built-in `turtle` module.

## Controls

| Key | Action |
|-----|--------|
| ↑ | Move up |
| ↓ | Move down |
| ← | Move left |
| → | Move right |

## What I Learned

- Structuring a small game using OOP principles (classes, composition vs. inheritance)
- Managing object state across frames in a game loop
- Decoupling responsibilities across files (movement, scoring, food spawning)
- Collision detection using coordinate distance checks
- Controlling animation speed and rendering with `screen.tracer()` and `screen.update()`

## Possible Future Improvements

- Add a restart/play again option after game over
- Increase snake speed as the score grows
- Save and display a high score between sessions
