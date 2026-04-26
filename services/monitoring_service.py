import random

def get_system_stats():
    return {
        "cpu": random.randint(10, 90),
        "ram": random.randint(20, 80),
        "disk": random.randint(30, 95),
        "status": "Healthy"
    }