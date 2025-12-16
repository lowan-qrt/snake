# Made by Nathan M. and Lowan Q.
# On December 2025
# Grid generator

def displayGrid(n: int, m: int, snake: list, listOfItem) -> None:
    """
    Generate the game grid.
    
    Args:
    n (int): X axe.
    m (int): Y axe.
    snake (list): The snake
    """
    grid = ''
    
    for i in range(n):
        for j in range(m):          
            if (j, i) in snake:
                if (j, i) == snake[0]:
                    print('■', end='')   # print head
                else:
                    print('□', end='')   # print body
            else:
                for item in listOfItem:
                    if (j,i) == item.coordinates:
                        match(item.name):
                            case 'apple':
                                 print(item.sprite,end='')  # print apple
                                 break
                            case 'bomb':
                                print(item.sprite,end='')   #print bomb
                                break    
                    elif item == listOfItem[-1]:
                        print('.', end='')                  # print grass    
                
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
    