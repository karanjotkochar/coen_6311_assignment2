# Random coordinates between a set radius
from ref_input import reference_coordinate
from gps_emulator import emulated_coordinates
from geopy.distance import geodesic
import random


# To calculate distance between two locations
def distance_func(coordinates_one, coordinates_two):
    distance = geodesic(coordinates_one, coordinates_two).m
    return distance


coordinates = emulated_coordinates()
final_coordinates = []

for key in coordinates:  # Generating coordinates within a set radius - limiting sample set
    d = distance_func(key, reference_coordinate())
    if d < 6:  # in m
        final_coordinates.append(key)
    else:
        continue


def test_coordinate():  # Randomly select coordinates from sample set - Test Coordinate
    random_coordinate = random.choice(final_coordinates)
    return random_coordinate
