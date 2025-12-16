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
        sprite (str): The item' sprite on the grid
    """
    def __init__(self, name,sprite):
        self.coordinates = (-1,-1)
        self.name = name
        self.sprite = sprite
    
    def itemPos(self, size_x, size_y,snakeCoordinates, itemsCoordinates):
        
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
        while ((x_pos,y_pos) in snakeCoordinates or (x_pos,y_pos) in itemsCoordinates):
            x_pos = random.randint(0,size_x-1)
            y_pos = random.randint(0,size_y-1)
           
        self.coordinates = (x_pos, y_pos)
        
     