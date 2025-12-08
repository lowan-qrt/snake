# Made by Nathan M. and Lowan Q.
# On December 2025
# Grid generator

def displayGrid(n: int, m: int, snake: list, apple: tuple) -> None:
    """
    Generate the game grid.
    
    Args:
    n (int): X axe.
    m (int): Y axe.
    snake (list): The snake object.
    apple (tuple): Coordinates of the apple.
    """
    grid = ''
    for i in range(n):
        for j in range(m):
            if (j, i) in snake:
                if (j, i) == snake[0]:
                    print('■', end='')   # print head
                else:
                    print('□', end='')   # print body
            elif (j,i) == apple:
                print('@',end='')        # print apple
            else:
                print('.', end='')       # print grass
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
    