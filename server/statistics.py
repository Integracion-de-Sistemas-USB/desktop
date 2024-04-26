import requests
import os
from dotenv import load_dotenv
from peripheral.constants import WIDTH, HEIGHT, HALF, ZERO, ERROR_POST, SUCCESS
from simulator.target_draw import calculate_distance
from simulator.angle_calculator import calculate_angle_two_dimension

def send_post_request(name, code, scores, stress, scenery, distance, weapon):
    load_dotenv()
    
    scores_array = [value for value in scores.values()]
    url = os.getenv("CREATE_URL")

    sample_data = {
        "code": code,
        "name": name,
        "score": scores_array,
        "gun": weapon,
        "scenary": {
            "bullet_weight": 5.0,
            "distance": distance,
            "ammo": "Sample Ammo",
            "scenary": scenery,
            "stress_level": stress,
            "caliber": 0.45
        }
    }

    response = requests.post(url, json=sample_data)
    verify_respond(response)

def get_scenery(scenery): 
    load_dotenv()
    url = os.getenv("SCENERY_URL") + scenery.lower()
    response = requests.get(url).json()
    return response[0]

def get_ammo(): 
    load_dotenv()
    url = os.getenv("SHOOT_URL") 
    response = requests.get(url).json()
    return response[0]

def send_coords_calculator(pointer_position, screen, stress, peripheral, scenery_name):
    load_dotenv()
    
    url = os.getenv("CALCULATE_URL")

    distance = calculate_distance(stress)

    w, h = screen.get_size()

    if peripheral:
        x = min(max((pointer_position[0] * w / HALF + screen.get_rect().centerx), ZERO), w)
        y = min(max((-pointer_position[1] * h / HALF + screen.get_rect().centery), ZERO), h)
    else:
        x = pointer_position[0]
        y = pointer_position[1]
    
    angle = calculate_angle_two_dimension(y, screen)
    
    data = {
        "x": x,
        "y": y,
        "target_distance": distance,
        "angle": -angle,
        "scenary": get_scenery(scenery_name),
        "ammo": get_ammo()
    }

    response = requests.post(url, json=data)
    if verify_respond(response):
        return response.json()
    else:
        return None

def verify_respond(response):
    if response.status_code == 200:
        return True
    else:
        print(f"{ERROR_POST}: {response.status_code}")
