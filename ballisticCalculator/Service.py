from WeaponCalculator import WeaponCalculator


class WeaponService:
    def __init__(self):
        self.calculator = WeaponCalculator()

    def perform_parabolic_shot(self, initial_velocity, angle, weapon_id):
        weapon_data = self.get_weapon_data(weapon_id)
        gravity = self.calculator.gravity_constant
        return self.calculator.parabolic_shot(initial_velocity, angle, gravity, weapon_data.get("caliber", 0))

    def perform_semiparabolic_shot(self, initial_velocity, angle, weapon_id):
        weapon_data = self.get_weapon_data(weapon_id)
        gravity = self.calculator.gravity_constant
        return self.calculator.semiparabolic_shot(initial_velocity, angle, gravity, weapon_data.get("caliber", 0))

    def calculate_affected_distance(self, perfect_distance, altitude, temperature_change_rate, sea_level_temperature, weapon_id):
        weapon_data = self.get_weapon_data(weapon_id)
        return self.calculator.calculate_effects_on_perfect_distance(weapon_data, perfect_distance, altitude, temperature_change_rate, sea_level_temperature)
