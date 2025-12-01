# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher
import snake
import grid

if __name__ == "__main__":
    try:
        # Size of the grid
        size_x = 10
        size_y = 10

        # Initialize snake
        snake = snake.Snake('Faker')
        snake.initializePos(size_x, size_y)

        running = True

        while running:
            # Update grid
            grid.createGrid(size_x, size_y, snake.coordinates)

            # Ask to move
            snake.move()
    except KeyboardInterrupt:
        print('\n\n\tFIN DU JEU\n')