# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher
import snake
import grid

if __name__ == "__main__":
    # Size of the grid
    size_x = 10
    size_y = 10

    # Initialize snake
    snake = snake.Snake()
    snake.initializePos(size_x, size_y)

    # Update grid
    grid.createGrid(size_x, size_y, snake.coordinates)