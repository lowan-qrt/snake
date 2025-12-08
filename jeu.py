# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher
import snake
import grid
import item

if __name__ == "__main__":
    print(r'   _________         _________')
    print(r'  /         \       /         \ ')
    print(r' /  /~~~~~\  \     /  /~~~~~\  \ ')
    print(r' |  |     |  |     |  |     |  |')
    print(r' |  |     |  |     |  |     |  |')
    print(r' |  |     |  |     |  |     |  |         /')
    print(r' |  |     |  |     |  |     |  |       //')
    print(r'(o  o)    \  \_____/  /     \  \_____/ /')
    print(r' \__/      \         /       \        /')
    print(r'  |         ~~~~~~~~~         ~~~~~~~~')
    print(r'  ^')
    print('\n\n\tWELCOME TO THE SNAKE GAME\n')
    print('\n\n\tBy Lowan Q. and Nathan M.\n')
    try:
        # Size of the grid
        size_x = 10
        size_y = 10

        # Initialize snake
        snake = snake.Snake(input('Saisir un pseudo : '))
        snake.initializePos(size_x, size_y)

        #Initialize apple
        apple = item.Item('Apple')
        apple.itemPos(size_x,size_y,snake.coordinates)

        running = True

        while running:
            if(len(snake.coordinates) >= (size_x * size_y)):
                print('\n\n\tFIN DU JEU BRAVO\n')
                break
                
            # Update grid
            grid.displayGrid(size_x, size_y, snake.coordinates,apple.coordinates)
            print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
            
            if(apple.coordinates == snake.coordinates[0]):
                apple.itemPos(size_x,size_y,snake.coordinates) 
                snake.grow()
                grid.displayGrid(size_x, size_y, snake.coordinates,apple.coordinates)
                
            # Ask to move
            snake.move(size_x, size_y)
    except KeyboardInterrupt:
        print('\n\n\tFIN DU JEU\n')