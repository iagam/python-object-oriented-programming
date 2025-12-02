from enemy import *

# V1 - Introduction to OOP - Instantiating Enemy Object
# enemy = Enemy()
# enemy.type_of_enemy = "Zombie"
# print(f"{enemy.type_of_enemy} has {enemy.health_points} and {enemy.attack_damage} attack damage")

# ---------------------------------------------------------------------------------------------

# V2 - Abstraction
# Abstarction means to hide implementation and only show necessary details to the user.
# User doesn't need to know what's going under the hood.

# zombie = Enemy()
# zombie.type_of_enemy = "Zombie"
# print(zombie.talk())
# print(zombie.walk_forward())
# print(zombie.attack())

# ---------------------------------------------------------------------------------------------

# V3 - Constructors
# zombie = Enemy("Zombie", 10, 1)
# big_zombie = Enemy("Big Zombie", 100, 10)

# print(zombie.attack())
# print(big_zombie.attack())
# print(
#     f"If user wants to change the Zombie to Ogre they can do that by zombie.type_of_enemy = 'Ogre'"
# )
# print("But we try not to encourage this functionality.")

# ---------------------------------------------------------------------------------------------

# V4 - Encapsulation
# Bundling of Data
# Change our public attributes to private
# Use double underscore to do that
# Getters and setters in encapsulation help in doing this
# Helps keep related fields and methods together

# zombie = Enemy("Zombie", 10, 1)
# big_zombie = Enemy("Big Zombie", 100, 10)


# print(zombie.get_type_of_enemy())
# print(big_zombie.get_type_of_enemy())

# ---------------------------------------------------------------------------------------------

# V5 - Inheritance
# Process of acquiring properties from one class to another
# Creates a hierarchy between classes
# Method overriding is when a child class has its own method already present in parent class.
# Self vs Super
# self is used to refer to the current object that is created or being instantiated, while
# super is used to refer to the parent class
# self is used when there is a need to differentiate between the instance variables
# and parameters with the same name, while
# super is used to call the parent class methods or constructors

from zombie import *
from ogre import *

# zombie = Zombie(10, 1)
# print(zombie.get_type_of_enemy())
# print(zombie.talk())
# print(zombie.spread_disease())

# ogre = Ogre(20, 3)
# print(ogre.get_type_of_enemy())
# print(ogre.talk())

# ---------------------------------------------------------------------------------------------

# V6 - Polymorphism
# Means to have many forms

# Create instances of different classes
ogre = Ogre(100, 10)
skeleton = Enemy("Skeleton", 15, 3)
zombie_a = Zombie(health_points=10, attack_damage=1)
zombie_b = Zombie(health_points=12, attack_damage=1)

# Create a list of heterogeneous objects
enemies_in_the_area = [ogre, skeleton, zombie_a, zombie_b]

print("--- Calling the same 'talk()' method on different objects ---")

# Iterate over the list and call talk() on each object
for enemy in enemies_in_the_area:
    print(f"Object Type: {enemy.get_type_of_enemy()}")
    enemy.talk()
    print("-" * 10)
