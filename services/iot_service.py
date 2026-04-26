import random

def get_environment_data():
    return {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "status": "Normal"
    }