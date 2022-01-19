import time
from ref_input import *
from gps_emulator_output import test_coordinate
from accelerometer_output import *
from gyroscope_output import *
from design import *

# Passing reference parameters - Attaching sensors
app = ConcreteSubject(reference_coordinate(),
                      gps_accuracy_limit(),
                      reference_accelerometer_value(),
                      reference_gyroscope_value())

# Defining users
user1 = ConcreteObserver("User 1")
user2 = ConcreteObserver("User 2")
user3 = ConcreteObserver("User 3")

# Attach users - User 1,2,3 should get update
app.register(user1)
app.register(user2)
app.register(user3)

# Deattach users - User 3 cancels registration - not get update, only user 1,2 get update
app.unregister(user3)

# Flag
theft_status = False


while not theft_status:
    gps_detect = app.get_distance(test_coordinate())  # Pass test parameters
    acc_detect = app.get_acceleration(test_accelerometer_value())
    gyro_detect = app.get_orientation(test_gyroscope_value())

    if gps_detect or acc_detect or gyro_detect == True:
        print("\n Notification Alert:")
        app.state_change()  # Calling state change function
        print("")
        break
    else:
        time.sleep(set_timer())
        continue
