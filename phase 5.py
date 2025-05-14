import time
import random

# Simulated sensor functions
def get_soil_moisture():
    return random.randint(20, 100)  # percentage

def get_temperature():
    return round(random.uniform(15.0, 40.0), 2)  # Celsius

def get_light_intensity():
    return random.randint(100, 1000)  # Lux

# Device control
class Device:
    def __init__(self, name, power_watt):
        self.name = name
        self.power_watt = power_watt
        self.status = False

    def turn_on(self):
        self.status = True
        print(f"{self.name} turned ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} turned OFF.")

    def power_usage(self, hours):
        return self.power_watt * hours if self.status else 0

# Devices
irrigation_pump = Device("Irrigation Pump", 100)
grow_lights = Device("Grow Lights", 60)
fan = Device("Ventilation Fan", 80)

def control_system():
    # Read sensor values
    soil_moisture = get_soil_moisture()
    temperature = get_temperature()
    light_intensity = get_light_intensity()

    print(f"\nSensor Readings - Soil Moisture: {soil_moisture}%, Temp: {temperature}°C, Light: {light_intensity} Lux")

    # Power management logic
    if soil_moisture < 40:
        irrigation_pump.turn_on()
    else:
        irrigation_pump.turn_off()

    if light_intensity < 300:
        grow_lights.turn_on()
    else:
        grow_lights.turn_off()

    if temperature > 30:
        fan.turn_on()
    else:
        fan.turn_off()

    # Calculate power usage (assuming 1 hour of operation for simplicity)
    total_power = sum([
        irrigation_pump.power_usage(1),
        grow_lights.power_usage(1),
        fan.power_usage(1)
    ])

    print(f"Total Power Used (1 hour): {total_power} Watt")

# Run the system every 5 seconds (simulation)
if __name__ == "__main__":
    try:
        while True:
            control_system()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSystem shutdown.")
