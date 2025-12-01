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
    def __init__(self, pseudo):
        self.coordinates = []
        self.pseudo = pseudo
        self.score = 0
    
    def initializePos(self, size_x, size_y):
        """
        Initialize the initial snake's position.

        Args:
            size_x (int): Length of the grid.
            size_y (int): Width of the grid.
        
        Returns:
            None
        """
        # Snake head
        x_pos_head = [x_pos for x_pos in range(size_x)][random.randint(1, size_x - 2)]
        y_pos_head = [x_pos for x_pos in range(size_y)][random.randint(1, size_y - 2)]
        self.coordinates.append((x_pos_head, y_pos_head))

        # Snake body
        x_pos_body = x_pos_head + [-1, 0, 1][random.randint(0,1)]
        if x_pos_body == x_pos_head:
            y_pos_body = y_pos_head + [-1, 1][random.randint(0,1)]
        else:
            y_pos_body = y_pos_head
        self.coordinates.append((x_pos_body, y_pos_body))

    def move(self):
        """
        Move the snake by using Z Q S D keys.

        Args:
            None
        
        Returns:
            None
        """
        last_tail = self.coordinates.pop()

        while True:
            next_move = input('Quel est votre prochain mouvement ? [Z, Q, S, D] ').upper()
            match next_move:
                case 'Z':
                    # Up
                    self.coordinates.insert(
                        0,
                        (self.coordinates[0][0] - 1, self.coordinates[0][1])
                    )
                case 'Q':
                    # Left
                    self.coordinates.insert(
                        0,
                        (self.coordinates[0][0], self.coordinates[0][1] - 1)
                    )
                case 'S':
                    # Down
                    self.coordinates.insert(
                        0,
                        (self.coordinates[0][0] + 1, self.coordinates[0][1])
                    )
                case 'D':
                    # Right
                    self.coordinates.insert(
                        0,
                        (self.coordinates[0][0], self.coordinates[0][1] + 1)
                    )
                case _:
                    self.coordinates.insert(1, last_tail)
                    print('\n\tMouvement invalide !\n')
            break