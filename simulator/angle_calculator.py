import pygame
import sys
from peripheral.constants import MAX_ANGLE

def calculate_angle_two_dimension(y, screen):
    w, h = screen.get_size()
    if y < h // 2:
        return MAX_ANGLE - (y / (h // 2) * MAX_ANGLE)
    elif y > h // 2:
        return -1 * (y - h // 2) / (h // 2) * MAX_ANGLE
    else:
        return 0
