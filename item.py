# Made by Nathan M. and Lowan Q.
# On December 2025
# Item configuration file
import random
import snake

class Item:
    """
    Represent an item in the game.

    Attributes:
        coordinates (tuple) : the item coordinates
        name (str): The item's name.
    """
    def __init__(self, name):
        self.coordinates = (-1,-1)
        self.name = name
    
    def itemPos(self, size_x, size_y,snakeCoordinates):
        
        """
        Initialize the item coordinates

        Args:
            size_x (int): Length of the grid.
            size_y (int): Width of the grid.
            snakeCoordinates (list of tuple) : coordinates of the snake
        
        Returns:
            None
        """
      
        x_pos = random.randint(0,size_x - 1)
        y_pos = random.randint(0,size_y - 1)
        while ((x_pos,y_pos) in snakeCoordinates):
            x_pos = random.randint(0,size_x-1)
            y_pos = random.randint(0,size_y-1)
           
        self.coordinates = ((x_pos, y_pos))
        
     