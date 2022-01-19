from ref_input import *
from gps_emulator_output import test_coordinate
from accelerometer_output import *
from gyroscope_output import *
from geopy.distance import geodesic


# Observer subject design pattern
class Subject:
    def register(self, observer):
        pass

    def unregister(self, observer):
        pass

    def notify(self, message):
        pass


class ConcreteSubject(Subject):

    state_change_gps = False
    state_change_acc = False
    state_change_gyro = False

    def __init__(self, reference_coordinate, gps_accuracy_limit, reference_value_acc, reference_value_gyro):
        self.observers = []
        self.ref_coords = reference_coordinate
        self.gps_limit = gps_accuracy_limit
        self.ref_acc = reference_value_acc
        self.ref_gyro = reference_value_gyro

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def get_distance(self, test_coordinate):
        distance = geodesic(self.ref_coords, test_coordinate).m

        if distance > self.gps_limit:
            print(f"Distance = {distance} greater than limit")
            self.state_change_gps = True
            return True

        else:
            print(f"Distance = {distance} within limit")
            return False

    def get_acceleration(self, test_value_acc):
        if abs(test_value_acc - self.ref_acc) > 0.05:
            print("Acceleration outside limit")
            self.state_change_acc = True
            return True

        else:
            print("Acceleration within limit")
            return False

    def get_orientation(self, test_value_gyro):
        if test_value_gyro <= self.ref_gyro:
            print("Gyroscope reading outside limit")
            self.state_change_gyro = True
            return True

        else:
            print("Gyroscope reading within limit")
            return False

    def state_change(self):
        if self.state_change_gps == True:
            self.notify("Theft detection by GPS")

        if self.state_change_acc == True:
            self.notify("Theft detection by Accelerometer Sensor")

        if self.state_change_gyro == True:
            self.notify("Theft detection by Gyroscope Sensor")


class Observer:
    def update(self):
        pass


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'"{self.name}" you have Notification :: {message}')
