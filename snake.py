# Made by Nathan M. and Lowan Q.
# On December 2025
# Snake configuration file
import random

class Snake:
    def __init__(self):
        self.coordinates = []
    
    def initializePos(self, size_x, size_y):
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