import pygame
import sys
import math
from peripheral.constants import ( 
    RED,
    BLACK,
    STRESS_LOW,
    STRESS_MEDIUM,
    STRESS_HIGH
)

target_coordinates = []

def draw_target(distance, screen):
    target_center = screen.get_rect().center

    base_radii = [30, 60, 90, 120, 150]

    scale_factor = 5 / distance

    scaled_radii = [r * scale_factor for r in base_radii]

    target_coordinates.append(target_center)

    for i, r in enumerate(scaled_radii):
        pygame.draw.circle(screen, BLACK, target_center, int(r), 2)
        points_on_circle = 50
        for theta in range(0, 360, 360 // points_on_circle):
            x = target_center[0] + int(r * math.cos(math.radians(theta)))
            y = target_center[1] + int(r * math.sin(math.radians(theta)))
            target_coordinates.append((x, y))

    pygame.draw.circle(screen, RED, target_center, 5)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Distance: {distance} meters", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_rect().centerx, 30))
    screen.blit(text, text_rect)

    pygame.display.flip()

def draw_target_with_distance(stress, screen):
    if stress == STRESS_LOW:
        distance = 10
    elif stress == STRESS_MEDIUM:
        distance = 20
    elif stress == STRESS_HIGH:
        distance = 50
    else:
        distance = 10

    draw_target(distance, screen)
