import requests

def send_post_request(pointer_position):
    url = "http://127.0.0.1:8000/results/create"
    
    sample_data = {
        "id": "test_id",
        "name": "Sample Name",
        "x": pointer_position[0],
        "y": pointer_position[1],
        "scenary": {
            "bullet_weight": 5.0,
            "distance": 100.0,
            "ammo": "Sample Ammo",
            "temperature": 25.0,
            "altitude": 500.0,
            "humidity": 50.0,
            "scenary": "Sample Scenary",
            "stress_level": 3,
            "caliber": 0.45
        }
    }

    response = requests.post(url, json=sample_data)
    
    if response.status_code == 201:
        print("Success.")
    else:
        print(f"Error in request POST: {response.status_code}")
