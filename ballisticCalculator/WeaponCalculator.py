import math

class WeaponCalculator:
    def __init__(self):
        self.AIR_DENSITY_SEA_LEVEL = 1.225
        self.GRAVITY_CONSTANT = 9.81 

    def parabolic_shot(self, initial_velocity, angle, gravity):
        angle_rad = math.radians(angle)
        range_ = (initial_velocity**2 * math.sin(2 * angle_rad)) / gravity
        max_height = (initial_velocity**2 * (math.sin(angle_rad))**2) / (2 * gravity)
        return range_, max_height

    def semiparabolic_shot(self, initial_velocity, angle, gravity):
        angle_rad = math.radians(angle)
        affected_range = (initial_velocity**2 * math.sin(2 * angle_rad)) / gravity
        max_height_affected = (initial_velocity**2 * (math.sin(angle_rad))**2) / (2 * gravity)
        return affected_range, max_height_affected

    def calculate_effects_on_perfect_distance(self, weapon_data, perfect_distance, altitude, temperature_change_rate, sea_level_temperature):
        if weapon_data:
            caliber = weapon_data.get("caliber", 0)
            resistance_factor = weapon_data.get("resistance_factor", 1.0)
            air_density_factor = self.AIR_DENSITY_SEA_LEVEL / self.calculate_air_density(altitude, temperature_change_rate, sea_level_temperature)
            temperature_factor = weapon_data.get("temperature_factor", 1.0)
            adjusted_perfect_distance = perfect_distance
            affected_distance = adjusted_perfect_distance * resistance_factor * air_density_factor * temperature_factor * caliber
            return affected_distance
        else:
            return None

    def calculate_air_density(self, altitude, temperature_change_rate, sea_level_temperature):
        adjusted_air_density = self.AIR_DENSITY_SEA_LEVEL * (1 - (temperature_change_rate * altitude) / sea_level_temperature)
        return adjusted_air_density if adjusted_air_density > 0 else 0  # Asegurar que la densidad del aire no sea negativa
