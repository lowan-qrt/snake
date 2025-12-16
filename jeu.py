# Made by Nathan M. and Lowan Q.
# On December 2025
# Game launcher
import snake
import grid
import item
import usualFunction as f
import random
import os


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
        snake = snake.Snake('Snake')

        snake.pseudo = f.validInput('str',1,100,'Enter your name','Snake')
        
        messageProbBomb = 'Enter the probability to generate a bomb when the snake eat an apple'
        probBomb = f.validInput('int',0,100,messageProbBomb,10)
        

        snake.initializePos(size_x, size_y)

        #Initialize items
        listOfItem = []
        
        apple = item.Item('apple','@')   
        apple.itemPos(size_x,size_y,snake.coordinates,listOfItem)     
        listOfItem.append(apple)
        scoreMultiplier = 1
        
        running = True


        while running:
            
            print(f'\t// DEBUG \\\\')
            print('snakeName:',snake.pseudo)
            print('probBomb:',probBomb)
            print('items coordinates and items sprites: ')
            print(listOfItem)
            for itemOnGrid in listOfItem:
                print(itemOnGrid.coordinates,itemOnGrid.sprite,itemOnGrid.name)
            print('nb bomb : ', f.occOfItem(listOfItem, 'bomb'))
            print('nb score multiplier:',scoreMultiplier)
            print(f'\t\\\\ DEBUG //\n')    
                
            if(len(snake.coordinates) >= (size_x * size_y)):
                print('\n\n\tEND OF THE GAME, GG!\n')
                # break
                
            # Update grid
            grid.displayGrid(size_x, size_y, snake.coordinates,listOfItem)
            print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
            
            scoreMultiplier = 1 + f.occOfItem(listOfItem, 'bomb')/10
            
            
            for itemOnGrid in listOfItem:
                if (itemOnGrid.coordinates == snake.coordinates[0]):
                
                    apple.itemPos(size_x,size_y,snake.coordinates,listOfItem) 
                    snake.eat(itemOnGrid,scoreMultiplier)
                    
                
                    if((random.randint(probBomb,100) == 100)):
                        listOfItem.append(item.Item('bomb','B'))
                        listOfItem[-1].itemPos(size_x,size_y,snake.coordinates,listOfItem)
                    
                    grid.displayGrid(size_x, size_y, snake.coordinates,listOfItem)
                    print(f'\t// SCORE \\\\\n{snake.pseudo} : {snake.score} pts')
                
            # Ask to move
            # fps = 1
            # fps += 1
            # print(fps%60)
            # print(fps)
            # if fps % 60 == 0:
            # os.system('cls')
            snake.move(size_x, size_y)
            
            
    except KeyboardInterrupt:
        print('\n\n\t'+snake.deathCause)
        print('\n\n\tEND OF THE GAME\n')
        score = snake.pseudo+ ': grid size: '+str(size_x)+' x '+str(size_y)+ ' score: '+str(snake.score) + ' Death by : '+snake.deathCause+'\n'
        highScore.write(score)
