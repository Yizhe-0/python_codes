'''
City, Country

Version: 0.1
Author: Yizhe
'''
def city_country(city, country, population=''):
    """Print the city and the country names."""
    if population:
        name = city + ', ' + country + ' - ' + population
    else:
        name = city + ', ' + country
    return name.title()

print(city_country('santiago', 'chile', 'population = 50000'))
