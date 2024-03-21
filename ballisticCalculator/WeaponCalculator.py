import math

class WeaponCalculator:
    def __init__(self):
        self.AIR_DENSITY_SEA_LEVEL = 1.225
        self.GRAVITY_CONSTANT = 9.81 

    def perfect_distance(self, initial_velocity, angle):
        angle_rad = math.radians(angle)
        distance = (initial_velocity ** 2 * math.sin(2 * angle_rad)) / self.GRAVITY_CONSTANT
        return distance

    def affected_distance(self, initial_velocity, angle, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        if weapon_data:
            caliber = weapon_data.get("caliber", 0)
            bullet_weight = weapon_data.get("bullet_weight", 0)
            resistance_factor = weapon_data.get("resistance_factor", 1.0)
            air_density_factor = self.AIR_DENSITY_SEA_LEVEL / self.calculate_air_density(altitude, temperature_change_rate, sea_level_temperature)
            temperature_factor = weapon_data.get("temperature_factor", 1.0)
            distance = self.perfect_distance(initial_velocity, angle)
            affected_distance = distance * resistance_factor * air_density_factor * temperature_factor * caliber * bullet_weight
            return affected_distance
        else:
            return None

    def calculate_air_density(self, altitude, temperature_change_rate, sea_level_temperature):
        adjusted_air_density = self.AIR_DENSITY_SEA_LEVEL * (1 - (temperature_change_rate * altitude) / sea_level_temperature)
        return max(adjusted_air_density, 0)  # Ensure air density is non-negative
    
    def simulate_horizontal_shot(self, initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        return self.simulate_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature, is_horizontal=True)

    def simulate_parabolic_shot(self, initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        return self.simulate_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature, is_horizontal=False)

    def simulate_shot(self, initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature, is_horizontal=True):
        angle_rad = math.radians(angle)
        vx = initial_velocity * math.cos(angle_rad)
        vy = initial_velocity * math.sin(angle_rad)
        
        trajectory = []
        t = 0
        while t <= total_time:
            x = vx * t
            y = vy * t - 0.5 * gravity * t ** 2
            z = 0 if is_horizontal else y  # For horizontal shot, z is 0
            trajectory.append((x, z, y))
            
            # Calculate drag force
            air_density = self.calculate_air_density(altitude, temperature_change_rate, sea_level_temperature)
            drag_force = 0.5 * air_density * vx ** 2 * weapon_data.get("drag_coefficient", 0) * weapon_data.get("cross_sectional_area", 0)
            
            # Apply drag force along x axis
            drag_force_x = drag_force / initial_velocity
            
            # Adjust velocities
            vx -= (drag_force_x / weapon_data.get("bullet_weight", 0)) * time_step
            vy -= (drag_force / initial_velocity + gravity) * time_step
            
            t += time_step
        
        return trajectory
