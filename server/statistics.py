import requests
import os
from dotenv import load_dotenv
from peripheral.constants import WIDTH, HEIGHT, HALF, ZERO

def send_post_request(pointer_position, screen):
    load_dotenv()
    
    url = os.getenv("CREATE_URL")
    
    sample_data = {
        "name": "Shoot Example Joycon Position",
        "x": min(max((pointer_position[0] * WIDTH / HALF + screen.get_rect().centerx), ZERO), WIDTH),
        "y": min(max((-pointer_position[1] * HEIGHT / HALF + screen.get_rect().centery), ZERO), HEIGHT),
        "scenery": {
            "bullet_weight": 5.0,
            "distance": 100.0,
            "ammo": "Sample Ammo",
            "temperature": 25.0,
            "altitude": 500.0,
            "humidity": 50.0,
            "scenery": "Sample Scenery",
            "stress_level": 3,
            "caliber": 0.45
        }
    }

    response = requests.post(url, json=sample_data)
    
    if response.status_code == 200:
        print("Success.")
    else:
        print(f"Error in request POST: {response.status_code}")
