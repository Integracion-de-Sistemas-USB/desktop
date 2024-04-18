import pygame
import math
from peripheral.constants import ( 
    RED,
    BLACK,
    STRESS_LOW,
    STRESS_MEDIUM,
    STRESS_HIGH,
    DISTANCE,
    METERS,
    POINTER_LOW_SIZE,
    POINTER_MEDIUM_SIZE,
    POINTER_HIGH_SIZE
)

target_coordinates = []

def calculate_distance(stress):
    if stress == STRESS_LOW:
        distance = 10
    elif stress == STRESS_MEDIUM:
        distance = 20
    elif stress == STRESS_HIGH:
        distance = 50
    else:
        distance = 10
    return distance

def calculate_scaled_radii(distance):
    base_radii = [30, 60, 90, 120, 150]
    scale_factor = 5 / distance
    return [r * scale_factor for r in base_radii]

def calculate_score(screen, collision_coordinate, stress, peripheral):
    distance = calculate_distance(stress)
    w, h = screen.get_size()
    target_center = (w // 2, h // 2)
    scaled_radii = calculate_scaled_radii(distance)

    if peripheral:
        x = collision_coordinate[0]
        y = collision_coordinate[1]
    else:
        x = collision_coordinate[0]
        y = collision_coordinate[1]
    
    distance_from_center = math.sqrt(
        (target_center[0] - x) ** 2 +
        (target_center[1] - y) ** 2)
    if distance_from_center > scaled_radii[-1] or distance != distance:
        score = 0
    else:
        for i, r in enumerate(scaled_radii):
            if distance_from_center <= r:
                score = max(0, 100 - int(distance_from_center))
                break
    return score

def draw_target(distance, screen, caption):
    w, h = screen.get_size()
    target_center = (w // 2, h // 2)

    scaled_radii = calculate_scaled_radii(distance)

    target_coordinates = []
    target_coordinates.append(target_center)

    for i, r in enumerate(scaled_radii):
        pygame.draw.circle(screen, BLACK, target_center, int(r), 2)
        points_on_circle = 50
        for theta in range(0, 360, 360 // points_on_circle):
            x = target_center[0] + int(r * math.cos(math.radians(theta)))
            y = target_center[1] + int(r * math.sin(math.radians(theta)))
            target_coordinates.append((x, y))

    if distance == 10:
        pygame.draw.circle(screen, RED, target_center, POINTER_LOW_SIZE)
    if distance == 20:
        pygame.draw.circle(screen, RED, target_center, POINTER_MEDIUM_SIZE)
    else:
        pygame.draw.circle(screen, RED, target_center, POINTER_HIGH_SIZE)

    font = pygame.font.SysFont(None, 36)
    if caption:
        text = font.render("Aim for the center of the target and press action button to calibrate the peripheral.", True, RED)
    else:
        text = font.render(f"{DISTANCE}: {distance} {METERS}", True, BLACK)
    text_rect = text.get_rect(center=(screen.get_rect().centerx, 30))
    screen.blit(text, text_rect)

def draw_target_with_distance(stress, screen):
    distance = calculate_distance(stress)
    draw_target(distance, screen, False)
