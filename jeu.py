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
        
        highScore = open('highscore.txt','a')
        
        # Size of the grid
        size_x = 10
        size_y = 10

        # Initialize snake
        snake = snake.Snake(input('Please, enter a pseudo: ') or 'Snake')
        snake.pseudo = playerName

        snake.initializePos(size_x, size_y)

        #Initialize apple
        apple = item.Item('apple')
        apple.itemPos(size_x,size_y,snake.coordinates)

        running = True

        while running:
            if(len(snake.coordinates) >= (size_x * size_y)):
                print('\n\n\tEND OF THE GAME, GG!\n')
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
        print('\n\n\t'+snake.deathCause)
        print('\n\n\tEND OF THE GAME\n')
        score = snake.pseudo+ ': grid size: '+str(size_x)+' x '+str(size_y)+ ' score: '+str(snake.score) + ' Death by : '+snake.deathCause+'\n'
        highScore.write(score)
