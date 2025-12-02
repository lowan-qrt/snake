# Made by Nathan M. and Lowan Q.
# On December 2025
# Grid generator

def createGrid(n, m, snake):
    grid = ''
    for i in range(n):
        for j in range(m):
            if(j, i) in snake:
                if(i,j) == snake[0]:
                    print('■', end='')   #print head
                else:
                    print('□', end='')   #print body
            else:
                print('.', end='')       #print grass
        print('\n')