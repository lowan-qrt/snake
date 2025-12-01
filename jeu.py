"""
@docstring
"""


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


if __name__ == "__main__":
    # grid = createGrid(5,6)
    snake = [(1,0),(2,0),(3,0)]
    createGrid(10,10,snake)
    