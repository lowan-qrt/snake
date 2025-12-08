# Made by Nathan M. and Lowan Q.
# On December 2025
# Snake configuration file
import random

class Snake:
    """
    Represent a player in the game (the snake).

    Attributes:
        coordinates (list (tuple)): List of the snake's (x, y) coordinates.
        pseudo (str): The player's name.
        score (int): The player's current score.
    """
    def __init__(self, pseudo: str):
        self.coordinates = []
        self.pseudo = 'Snake'
        self.score = 0
        self.last_move = None
        self.deathCause = 'Abort Program'
    
    def initializePos(self, size_x: int, size_y: int) -> None:
        """
        Initialize the initial snake's position.

        Args:
            self: The object.
            size_x (int): Length of the grid.
            size_y (int): Width of the grid.
        
        Returns:
            None
        """
        # Snake head
        # Snake's head
        x_pos_head = [x_pos for x_pos in range(size_x)][random.randint(1, size_x - 2)]
        y_pos_head = [x_pos for x_pos in range(size_y)][random.randint(1, size_y - 2)]
        self.coordinates.append((x_pos_head, y_pos_head))

        # Snake body
        x_pos_body = x_pos_head + [-1, 0, 1][random.randint(0,1)]
        # Snake's body
        x_pos_body = x_pos_head + [-1, 0, 1][random.randint(0,2)]
        if x_pos_body == x_pos_head:
            y_pos_body = y_pos_head + [-1, 1][random.randint(0,1)]
        else:
            y_pos_body = y_pos_head
        self.coordinates.append((x_pos_body, y_pos_body))

        # Determine the first cancel move
        if self.coordinates[0][1] < self.coordinates[1][1]:
            self.last_move = 'Z'
        elif self.coordinates[0][1] > self.coordinates[1][1]:
            self.last_move = 'S'
        elif self.coordinates[0][0] < self.coordinates[1][0]:
            self.last_move = 'Q'
        else:
            self.last_move = 'D'
    
    def grow(self) -> None:
        """
        After eating an apple, the snake will grow
        Args:
            self: The object.
        
        Returns:
            None
        """
        self.coordinates.append(self.coordinates[-1])
        self.score = self.score + 1
 
    def move(self, grid_x: int, grid_y: int) -> None:
        """
        Move the snake by using Z Q S D keys.

        Args:
            grid_x (int): Length of the X axe.
            grid_y (int): Length of the Y axe.
            self: The object.

        Returns:
            None
        """
        last_tail = self.coordinates.pop()

        while True:
            next_move = input(f'{self.pseudo}, what\'s your next movement? [Z, Q, S, D] ').upper()
            match next_move:
                case 'Z':
                    if self.last_move != 'S':
                        self.coordinates.insert(
                            0,
                            (self.coordinates[0][0], self.coordinates[0][1] - 1)
                        )
                        self.last_move = next_move
                    else:
                        self.coordinates.append(last_tail)
                case 'Q':
                    if self.last_move != 'D':
                        self.coordinates.insert(
                            0,
                            (self.coordinates[0][0] - 1, self.coordinates[0][1])
                        )
                        self.last_move = next_move
                    else:
                        self.coordinates.append(last_tail)
                case 'S':
                    if self.last_move != 'Z':
                        self.coordinates.insert(
                            0,
                            (self.coordinates[0][0], self.coordinates[0][1] + 1)
                        )
                        self.last_move = next_move
                    else:
                        self.coordinates.append(last_tail)
                case 'D':
                    if self.last_move != 'Q':
                        self.coordinates.insert(
                            0,
                            (self.coordinates[0][0] + 1, self.coordinates[0][1])
                        )
                        self.last_move = next_move
                    else:
                        self.coordinates.append(last_tail)
                case _:
                    self.coordinates.insert(1, last_tail)
                    print('\n\Invalid movement!\n')
            Snake.detectCollision(self, grid_x, grid_y)
            break
    
    def detectCollision(self, grid_x: int, grid_y: int) -> None:
        """
        Detect wall and body collisions.
        
        Args:
            grid_x (int): Length of the X axe.
            grid_y (int): Length of the Y axe.
            self: The object.

        Returns:
            None
        """
        # Wall collisions
        if (self.coordinates[0][0] > grid_x - 1 or self.coordinates[0][0] < 0 or self.coordinates[0][1] < 0 or self.coordinates[0][1] > grid_y - 1):
            print('\n\tYou lose!')
            self.deathCause = 'The snake eat the wall'
            raise KeyboardInterrupt
        # Body collisions
        elif (self.coordinates[0] in self.coordinates[1:]):
            print('\n\tYou lose!')
            self.deathCause = 'The snake eat itself'
            raise KeyboardInterrupt