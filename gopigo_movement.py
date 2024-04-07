# import the GoPiGo3 drivers
import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor()

while True:
    # Directly print the values of the sensor.
    gpg.forward()
    distance = my_distance_sensor.read_mm()
    print("Distance Sensor (mm): " + str(distance))
    if(my_distance_sensor.read_mm() <= 100):
        print("Obstacle !!!")