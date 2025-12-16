# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher

import snake as sn
import grid
import item
from playsound3 import playsound
import menu

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
    print('\n\tBy Lowan Q. and Nathan M.\n')

    play = True
    while play:
        play = menu.main()

        # Play the game
        if play == True:
            try:
                # Load or reload last scores
                highScore = open('assets/highscore.txt', 'a')
                    
                # Set the grid
                size_x = 10
                size_y = 10

                # Initialize snake
                snake = sn.Snake()
                try:
                    snake.pseudo = input('\nEnter your name: ') or 'Snake'
                except KeyboardInterrupt:
                    continue
                snake.initializePos(size_x, size_y)

                # Initialize apple
                apple = item.Item('apple')
                apple.itemPos(size_x,size_y,snake.coordinates)

                # Run the game
                running = True
                while running:
                    # Winning
                    if(len(snake.coordinates) >= (size_x * size_y)):
                        print('\n\n\tYOU WIN, GG!\n')
                        break
                        
                    # Update grid
                    grid.displayGrid(size_x, size_y, snake.coordinates,apple.coordinates)

                    # Print scores
                    print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                    
                    # Eat apple
                    if(apple.coordinates == snake.coordinates[0]):
                        apple.itemPos(size_x,size_y,snake.coordinates) 
                        snake.grow()
                        playsound("assets/eat_apple_sound_effect.mp3")
                        grid.displayGrid(size_x, size_y, snake.coordinates,apple.coordinates)
                        print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                    
                    # Ask to move
                    snake.move(size_x, size_y)
            except KeyboardInterrupt:
                # Save scores
                score = snake.pseudo + ': grid size: ' + str(size_x) + ' x ' + str(size_y) + ' score: ' + str(snake.score) + ' Death by : ' + snake.deathCause + '\n'
                highScore.write(score)
                highScore.close()
                continue 

        # Exit the game
        else:
            play == menu.quit()
    print('\n\n\tEND OF THE GAME\n')
