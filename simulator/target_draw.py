import pygame
import sys
import math
from peripheral.constants import ( 
    RED,
    BLACK,
    STRESS_LOW,
    STRESS_MEDIUM,
    STRESS_HIGH,
    HALF,
    ZERO,
    SCORE,
    DISTANCE,
    METERS
)

target_coordinates = []

def draw_target(distance, screen, collision_distance=None, collision_coordinate=None):
    w, h = pygame.display.get_surface().get_size()
    target_center = (w // 2, h // 2)

    base_radii = [30, 60, 90, 120, 150]

    scale_factor = 5 / distance

    scaled_radii = [r * scale_factor for r in base_radii]

    target_coordinates.append(target_center)

    if collision_distance is not None and collision_coordinate is not None:
        distance_from_center = math.sqrt((target_center[0] - (min(max((collision_coordinate[0] * w / HALF + screen.get_rect().centerx), ZERO), w))) ** 2 +
                                         (target_center[1] - (min(max((-collision_coordinate[1] * h / HALF + screen.get_rect().centery), ZERO), h))) ** 2)
        if distance_from_center > scaled_radii[-1] or distance != collision_distance:
            score = 0
        else:
            for i, r in enumerate(scaled_radii):
                if distance_from_center <= r:
                    score = max(0, 100 - int(distance_from_center))
                    break
        print(f"{SCORE}: {score}")
        pygame.draw.circle(screen, RED, collision_coordinate, 5)

    for i, r in enumerate(scaled_radii):
        pygame.draw.circle(screen, BLACK, target_center, int(r), 2)
        points_on_circle = 50
        for theta in range(0, 360, 360 // points_on_circle):
            x = target_center[0] + int(r * math.cos(math.radians(theta)))
            y = target_center[1] + int(r * math.sin(math.radians(theta)))
            target_coordinates.append((x, y))

    pygame.draw.circle(screen, RED, target_center, 5)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"{DISTANCE}: {distance} {METERS}", True, BLACK)
    text_rect = text.get_rect(center=(w // 2, h - 30))
    screen.blit(text, text_rect)

def draw_target_with_distance(stress, screen, collision_coordinate=None):
    if stress == STRESS_LOW:
        distance = 10
    elif stress == STRESS_MEDIUM:
        distance = 20
    elif stress == STRESS_HIGH:
        distance = 50
    else:
        distance = 10

    draw_target(distance, screen, distance, collision_coordinate)
