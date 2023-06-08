# Importing an entire module.
import car1

my_mustang = car1.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car1.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())