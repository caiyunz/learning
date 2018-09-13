#!/usr/bin/python3
def get_city_country_name(city,country,population=''):
    City=city.title()
    Country=country.title()
    if population:
        name=City+","+Country+" - population "+str(population)
    else:
        name=City+","+Country
    return(name)
