# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher

import snake as sn
import grid
import item
import usualFunction as f
import random
import os
from playsound3 import playsound
import menu
import time

if __name__ == "__main__":
    os.system('cls')
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
                    snake.pseudo = input('\nEnter your name: ')
                except KeyboardInterrupt:
                    continue
                snake.initializePos(size_x, size_y)
                               
                messageProbBomb = 'Enter the probability to generate a bomb when the snake eat an apple'
                probBomb = f.validInput('int',0,100,messageProbBomb,10)

                #Initialize items
                listOfItem = []
                
                apple = item.Item('apple','@')   
                apple.itemPos(size_x,size_y,snake.coordinates,listOfItem)     
                listOfItem.append(apple)
                scoreMultiplier = 1
                
                #Run the game
                running = True
                while running:
                                  
                    # Winning
                    if(len(snake.coordinates) >= (size_x * size_y)):
                        print('\n\n\tYOU WIN, GG!\n')
                        break
                        
                    # Update grid
                    grid.displayGrid(size_x, size_y, snake.coordinates,listOfItem)

                    # Print scores
                    print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                    
                    # Eat Item
                    for itemOnGrid in listOfItem:
                        if(itemOnGrid.coordinates == snake.coordinates[0]):
                            apple.itemPos(size_x,size_y,snake.coordinates,listOfItem) 
                            snake.eat(itemOnGrid,scoreMultiplier)
                
                            if((random.randint(probBomb,100) == 100)):
                                listOfItem.append(item.Item('bomb','B'))
                                listOfItem[-1].itemPos(size_x,size_y,snake.coordinates,listOfItem)
                            os.system('cls')
                            grid.displayGrid(size_x, size_y, snake.coordinates,listOfItem)
                            print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                            
                        scoreMultiplier = 1 + f.occOfItem(listOfItem, 'bomb')/10
                   

                    
                    time.sleep(0.1)



                    os.system('cls')
                    snake.move2(size_x, size_y)
               
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