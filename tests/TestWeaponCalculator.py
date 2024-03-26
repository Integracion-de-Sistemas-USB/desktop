import unittest

from ballisticCalculator.WeaponCalculator import WeaponCalculator

class TestWeaponCalculator(unittest.TestCase):
    def setUp(self):
        self.weapon_calculator = WeaponCalculator()

    def test_perfect_distance(self):     
        initial_velocity = 100  
        angle = 45  
        expected_distance = 1019.36799  
        calculated_distance = self.weapon_calculator.perfect_distance(initial_velocity, angle)
        self.assertAlmostEqual(calculated_distance, expected_distance, delta=0.1)  

    def test_affected_distance(self):
        initial_velocity = 100  # m/s
        angle = 45  # degrees
        weapon_data = {"caliber": 0.5, "bullet_weight": 0.02, "resistance_factor": 0.8, "temperature_factor": 1.2}
        altitude = 5000  # meters
        temperature_change_rate = 0.0065  # K/m
        sea_level_temperature = 288.15  # K
        expected_affected_distance = 11.029988319035667  
        calculated_affected_distance = self.weapon_calculator.affected_distance(initial_velocity, angle, weapon_data, altitude, temperature_change_rate, sea_level_temperature)
        self.assertAlmostEqual(calculated_affected_distance, expected_affected_distance, delta=0.1)  # Adjusted tolerance
    
    def test_calculate_air_density(self):
        altitude = 5000  
        temperature_change_rate = 0.0065  
        sea_level_temperature = 288.15  
        expected_air_density = 1.086834 
        calculated_air_density = self.weapon_calculator.calculate_air_density(altitude, temperature_change_rate, sea_level_temperature)
        self.assertAlmostEqual(calculated_air_density, expected_air_density, delta=0.1)  

    def test_simulate_horizontal_shot(self):
        
        initial_velocity = 100  
        angle = 45  
        gravity = 9.81  
        time_step = 0.1  
        total_time = 10  
        weapon_data = {"drag_coefficient": 0.2, "cross_sectional_area": 0.01, "bullet_weight": 0.02}
        altitude = 5000  
        temperature_change_rate = 0.0065  
        sea_level_temperature = 288.15  
        trajectory = self.weapon_calculator.simulate_horizontal_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature)
        
        self.assertAlmostEqual(trajectory[0][0], 0, delta=0.1)  
        self.assertAlmostEqual(trajectory[0][1], 0, delta=0.1)  
        self.assertAlmostEqual(trajectory[-1][0], 510.358 , delta=10)  

    def test_simulate_parabolic_shot(self):
        
        initial_velocity = 100  
        angle = 45  
        gravity = 9.81  
        time_step = 0.1  
        total_time = 10  
        weapon_data = {"drag_coefficient": 0.2, "cross_sectional_area": 0.01, "bullet_weight": 0.02}
        altitude = 5000  
        temperature_change_rate = 0.0065  
        sea_level_temperature = 288.15  
        trajectory = self.weapon_calculator.simulate_parabolic_shot(initial_velocity, angle, gravity, time_step, total_time, weapon_data, altitude, temperature_change_rate, sea_level_temperature)
        
        self.assertAlmostEqual(trajectory[0][0], 0, delta=0.1)  
        self.assertAlmostEqual(trajectory[0][1], 0, delta=0.1)  
        self.assertAlmostEqual(trajectory[-1][0], 510.358, delta=10)  

if __name__ == '__main__':
    unittest.main()
