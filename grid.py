# Made by Nathan M. and Lowan Q.
# On December 2025
# Main file to lauch the game

def createGrid(n,m,snake):
    grid = ''
    for i in range(n):
        for j in range(m):
            if(i,j) in snake:
                if(i,j) == snake[0]:
                    print('■',end='')   #print head
                else:
                    print('□',end='')   #print body
            else:
                print('.',end='')       #print grass
        print('\n')

