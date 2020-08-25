import unittest
from city_functions11_1 import city_country

class CityTests(unittest.TestCase):
    """Test for 'city_functions11_1.py"""

    def test_city_country(self):
        """Do 'shenzhen, china' work?"""
        city_country_name = city_country('chicago', 'america')
        self.assertEqual(city_country_name, 'Chicago, America')
    
    def test_city_population(self):
        """Test if population() works."""
        city_country_name = city_country('santiago', 'chile', 'population = 50000')
        self.assertEqual(city_country_name, 'Santiago, Chile - Population = 50000')
unittest.main()