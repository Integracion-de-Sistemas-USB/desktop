import requests
import os
from dotenv import load_dotenv
from peripheral.constants import WIDTH, HEIGHT, HALF, ZERO, ERROR_POST, SUCCESS
from simulator.target_draw import calculate_distance
from simulator.angle_calculator import calculate_angle_two_dimension

def send_post_request(pointer_position, screen, name, code):
    load_dotenv()
    
    url = os.getenv("CREATE_URL")

    w, h = screen.get_size()
    
    sample_data = {
        "name": name,
        "code": code,
        "x": min(max((pointer_position[0] * w / HALF + screen.get_rect().centerx), ZERO), w),
        "y": min(max((-pointer_position[1] * h / HALF + screen.get_rect().centery), ZERO), h),
        "scenary": {
            "bullet_weight": 5.0,
            "distance": 100.0,
            "ammo": "Sample Ammo",
            "temperature": 25.0,
            "altitude": 500.0,
            "humidity": 50.0,
            "scenary": "Sample Scenery",
            "stress_level": 3,
            "caliber": 0.45
        }
    }

    response = requests.post(url, json=sample_data)
    
    verify_respond(response)

def send_coords_calculator(pointer_position, screen, stress):
    load_dotenv()
    
    url = os.getenv("CALCULATE_URL")

    distance = calculate_distance(stress)

    w, h = screen.get_size()

    x = min(max((pointer_position[0] * w / HALF + screen.get_rect().centerx), ZERO), w)
    y = min(max((-pointer_position[1] * h / HALF + screen.get_rect().centery), ZERO), h)
    angle = calculate_angle_two_dimension(y, screen)

    data = {
        "initial_velocity": 1000,
        "x": x,
        "y": y,
        "target_distance": distance,
        "angle": -angle
    }

    response = requests.post(url, json=data)
    if verify_respond(response):
        return response.json()
    else:
        return None

def verify_respond(response):
    if response.status_code == 200:
        print(f"{SUCCESS}.")
        return True
    else:
        print(f"{ERROR_POST}: {response.status_code}")
