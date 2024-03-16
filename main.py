import pygame
from pygame.locals import *
import time
from peripheral.constants import *
from peripheral.shoot_draw import *

pygame.init()

pygame.display.set_caption(CAPTION)

red_points = []

def main():
    try:
        try:
            from peripheral.external_peripheral import ExternalPeripheral
            peripheral = ExternalPeripheral()
        except Exception as e:
            print(INITIALIZATION_ERROR, e)
            peripheral = None

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            screen.fill(SCREEN_FILL)

            if peripheral:
                try:
                    pointer_position = peripheral.get_pointer_position()
                    if peripheral.get_button_events():
                        red_points.append(pointer_position)
                except Exception as e:
                    print(READING_ERROR, e)
                    peripheral = None
            else:
                pointer_position = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    red_points.append(pointer_position)

            if peripheral:
                draw_peripheral_pointer(pointer_position, WHITE)
            else:
                draw_mouse_pointer(pointer_position, WHITE)
            draw_shoots(red_points, RED, peripheral)

            pygame.display.flip()
            time.sleep(POINTER_REFRESH_TIME)
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
