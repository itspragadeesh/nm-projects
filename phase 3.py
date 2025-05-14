import time
import random

# Simulated device power consumption (watts)
DEVICE_POWER = {
    'irrigation_pump': 120,
    'greenhouse_lights': 60,
    'sensor_hub': 15
}

# Simulated solar power generation (watts)
def get_solar_power():
    # Simulate solar input varying over the day
    hour = time.localtime().tm_hour
    if 6 <= hour <= 18:
        return random.randint(100, 300)  # Simulated solar power during the day
    return 0  # Night time

# Simulated soil moisture sensor
def get_soil_moisture():
    return random.uniform(0, 1)  # 0 = dry, 1 = wet

# Energy balance logic
def should_activate_device(device, available_power):
    return DEVICE_POWER[device] <= available_power

# Main control loop
def run_power_management():
    while True:
        solar_power = get_solar_power()
        soil_moisture = get_soil_moisture()

        print(f"\nAvailable Solar Power: {solar_power}W")
        print(f"Soil Moisture Level: {soil_moisture:.2f}")

        active_devices = []

        # Priority 1: Sensor Hub (always try to keep on)
        if should_activate_device('sensor_hub', solar_power):
            active_devices.append('sensor_hub')
            solar_power -= DEVICE_POWER['sensor_hub']

        # Priority 2: Irrigation if soil is dry
        if soil_moisture < 0.4 and should_activate_device('irrigation_pump', solar_power):
            active_devices.append('irrigation_pump')
            solar_power -= DEVICE_POWER['irrigation_pump']

        # Priority 3: Greenhouse lights at night
        hour = time.localtime().tm_hour
        if solar_power > 0 and (hour < 6 or hour > 18):
            if should_activate_device('greenhouse_lights', solar_power):
                active_devices.append('greenhouse_lights')
                solar_power -= DEVICE_POWER['greenhouse_lights']

        print(f"Activated Devices: {active_devices}")
        print(f"Remaining Power: {solar_power}W")

        time.sleep(5)  # Simulate periodic monitoring

# Run the simulation
if __name__ == "__main__":
    try:
        run_power_management()
    except KeyboardInterrupt:
        print("Power management simulation stopped.")
