# Made by Nathan M. and Lowan Q.
# On December 2025
# Main file to lauch the game

def displayGrid(n,m,snake):
    """
    Display a grid of n times m units.
    
    Args:
        n (int): number of lines
        m (int): number of rows
        snake (list of coordinates (tuples)): coordinates of all part of the snake
        
    Returns:
        None, it just print all element of the game
    """
    grid = ''
    for i in range(n):
        for j in range(m):
            if(j,i) in snake:
                if(j,i) == snake[0]:
                    print('■',end='')   #print head
                else:
                    print('□',end='')   #print body
            else:
                print('.',end='')       #print grass
        print('\n')

def displayCircle(r,snake):
    """
    Display the grid as a circle
    
    Args:
        r (int) : radius (min : 5) 
    """
    
    n = 2 * r + 1
    for i in range(n ):
        for j in range(n):
          
       
            dx = (j ) - r
            dy = (i ) - r
            distance = (dx**2 + dy**2)**0.5
            if distance <= r - 0.5:
                print('.', end='')
            else:
                print('▓', end='')
        print('\n')
    
    # for i in range(r*2+3):
        # for j in range(r*2+3):
            # if(i,j) in snake:
                # if(i,j) == snake[0]:
                    # print('■',end='')   #print head
                # else:
                    # print('□',end='')   #print body
            # else:
                
                # if ((i <= 2 and j <=1) or (i <= 1 and j <=2) or (i <= 2 and j >=r*2+1) or (i <= 1 and j >=r*2) or (i >= r*2 and j <=1) or (i >= r*2+1 and j <=2) or  (i >= r*2 and j >=r*2+1) or (i >= r*2+1 and j >=r*2) or (i == 0) or (j == 0) or (i == 2*r+2) or (j == 2*r+2)):
                # if ((i,j) in grassZone):    
                    # print('.',end='') #print grass                   
                # else:
                    # print('▓',end='')       #print wall
        # print('\n')

    
# def maze(m,n, snake):   #Si on a le temps car ça à l'air galère à faire, mais fun
    