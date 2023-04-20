#here giving values for characters
cars=100
space_in_a_car=4
drivers=30
passengers=90
#play with characters which are given specific value
cars_not_drive=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passenger_per_car=passengers/cars_driven

print("There are",cars,"cars available.")
print("There are only", drivers ,"drivers available.")
print("There will be", cars_not_drive ,"empty cars today.")
print("We acan transport", carpool_capacity ,"people today.")
print("We", passengers ,"to carpool today.")
print("We need to put about", average_passenger_per_car ,"in each car.")
