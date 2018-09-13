#!/usr/bin/python3
import city_function
import unittest
class test_city_country_name(unittest.TestCase):

    def test_city_country(self):
        name=city_function.get_city_country_name('santiago','chile')
        self.assertEqual(name,'Santiago,Chile')
    
    def test_city_country_population(self):
        name=city_function.get_city_country_name('santiago','chile',5000000)
        self.assertEqual(name,'Santiago,Chile - population 5000000')
unittest.main()
