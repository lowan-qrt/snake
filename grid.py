# Made by Nathan M. and Lowan Q.
# On December 2025
# Grid generator

def createGrid(n, m, snake):
    grid = ''
    for i in range(n):
        for j in range(m):
            if (i, j) in snake:
                if (i, j) == snake[0]:
                    print('■', end='')   #print head
                else:
                    print('□', end='')   #print body
            else:
                print('.', end='')       #print grass
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
    
# def maze(m,n, snake):   #Si on a le temps car ça à l'air galère à faire, mais fun
    