import random
import time
import logging
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, filename='agri_power.log', filemode='w',
                    format='%(asctime)s  %(levelname)s  %(message)s')

# Simulate sensor data
def read_sensor_data():
    return {
        "soil_moisture": random.randint(20, 80),  # % moisture
        "temperature": random.uniform(20, 40),    # °C
        "weather_forecast": random.choice(["sunny", "rainy", "cloudy"]),
        "motor_usage_hours": random.randint(0, 6)  # hours
    }

# Train mock ML model
def train_energy_model():
    X = np.array([[25, 1], [30, 2], [35, 4], [28, 3]])
    y = np.array([2.5, 3.5, 6.0, 4.0])  # energy usage in kWh
    model = LinearRegression().fit(X, y)
    return model

# Smart energy distribution
def smart_power_allocation(sensor_data, energy_model):
    features = np.array([[sensor_data['temperature'], sensor_data['motor_usage_hours']]])
    predicted_energy = energy_model.predict(features)[0]

    irrigation_needed = sensor_data['soil_moisture'] < 40

    power_distribution = {
        "irrigation_motor": predicted_energy if irrigation_needed else 0,
        "sensor_units": 0.5,
        "control_unit": 0.3
    }

    logging.info(f"Sensor Data: {sensor_data}")
    logging.info(f"Predicted Energy Requirement: {predicted_energy:.2f} kWh")
    logging.info(f"Power Distribution Plan: {power_distribution}")
    return power_distribution

# Simulation
def run_simulation_cycle():
    model = train_energy_model()
    for _ in range(5):
        sensor_data = read_sensor_data()
        allocation = smart_power_allocation(sensor_data, model)
        print(f"Cycle at {datetime.now().strftime('%H:%M:%S')}: {allocation}")
        time.sleep(2)

if __name__ == "__main__":
    run_simulation_cycle()
