from WeaponCalculator import WeaponCalculator


class WeaponService:
    def __init__(self):
        self.weapon_calculator = WeaponCalculator()

    def calculate_perfect_distance(self, initial_velocity, angle):
        return self.weapon_calculator.perfect_distance(initial_velocity, angle)

    def calculate_affected_distance(self, initial_velocity, angle, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        return self.weapon_calculator.affected_distance(initial_velocity, angle, weapon_data, altitude, temperature_change_rate, sea_level_temperature)

    def simulate_horizontal_shot(self, initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        return self.weapon_calculator.simulate_horizontal_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature)

    def simulate_parabolic_shot(self, initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature):
        return self.weapon_calculator.simulate_parabolic_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature)
