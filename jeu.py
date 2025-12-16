# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher

import snake as sn
import grid
import item
import usualFunction as f
import menu

import random
import os
import sys
from playsound3 import playsound
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
        f.hideCursor(False)
        play = menu.main()

        # Play the game
        if play == True:
            try:
                # Load or reload last scores
                highScore = open('assets/highscore.txt', 'a')
                  
                #Set the gamemode
                warped = f.validInput('int', 0, 1, 'Warped grid ? (Yes -> 1 / False -> 0)', 0)
                movementMethod = f.validInput('int', 0, 3, 'Movement Method (with interuption -> 1 / without interuption -> 2)', 2)
                  
                # Set the grid      
                size_x = f.validInput('int', 10, 24, '\nNumber of rows (min: 10 max: 24)', 10)
                size_y = f.validInput('int', 10, 24, 'Number of columns (min: 10 max: 24)', 10)
                              
                # Initialize snake
                snake = sn.Snake()
                try:
                    snake.pseudo = input('\nEnter your name: ')
                except KeyboardInterrupt:
                    continue
                snake.initializePos(size_x, size_y)
                     
                #Initialize items
                listOfItem = []
                messageProbBomb = 'Enter the probability to generate a bomb when the snake eat an apple'
                probBomb = f.validInput('int', 0, 100, messageProbBomb, 10)
                      
                apple = item.Item('apple','@')   
                apple.itemPos(size_x, size_y, snake.coordinates, listOfItem)    
                listOfItem.append(apple)
                
                scoreMultiplier = 1
                
                #Hide Cursor
                if (os.name == 'nt'):
                    f.hideCursor(True)
                
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
                            #Regeneration of the apple
                            apple.itemPos(size_x, size_y, snake.coordinates, listOfItem) 
                            #Apply item effect on the snake
                            snake.eat(itemOnGrid, scoreMultiplier)
                
                            #Randomly generate a bomb
                            if((random.randint(probBomb,100) == 100)): 
                                
                                listOfItem.append(item.Item('bomb', 'B'))
                                listOfItem[-1].itemPos(size_x, size_y, snake.coordinates, listOfItem)
                            
                            #Update grid to display generated item
                            os.system('cls')
                            grid.displayGrid(size_x, size_y, snake.coordinates,listOfItem)
                            print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                        
                        #The more the bombs there are, the more the score multiplier is high
                        scoreMultiplier = 1 + f.occOfItem(listOfItem, 'bomb')/10
                           
                    #Speed of the game
                    time.sleep(0.1)

                    #Clear the CLI for better visibility of the game
                    
                    
                    #Ask the snake to move
                    match(movementMethod):
                        case 1 :
                            snake.move(size_x, size_y, warped)
                            os.system('cls')
                        case 2:
                            snake.move2(size_x, size_y, warped)
                            os.system('cls')
               
            except KeyboardInterrupt:
                # Save scores
                score = snake.pseudo + ': grid size: ' + str(size_x) + ' x ' + str(size_y) + ' score: ' + str(snake.score) + ' Death by : ' + snake.deathCause + '\n'             

                highScore.close()
                continue 

        # Exit the game
        else:
            play == menu.quit()
    print('\n\n\tEND OF THE GAME\n')
    f.hideCursor(False)