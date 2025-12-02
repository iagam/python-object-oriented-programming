from enemy import *

# V1 - Introduction to OOP - Instantiating Enemy Object
# enemy = Enemy()
# enemy.type_of_enemy = "Zombie"
# print(f"{enemy.type_of_enemy} has {enemy.health_points} and {enemy.attack_damage} attack damage")

# V2 - Abstraction
# Abstarction means to hide implementation and only show necessary details to the user.
# User doesn't need to know what's going under the hood.

# zombie = Enemy()
# zombie.type_of_enemy = "Zombie"
# print(zombie.talk())
# print(zombie.walk_forward())
# print(zombie.attack())

# V3 - Constructors
# zombie = Enemy("Zombie", 10, 1)
# big_zombie = Enemy("Big Zombie", 100, 10)

# print(zombie.attack())
# print(big_zombie.attack())
# print(
#     f"If user wants to change the Zombie to Ogre they can do that by zombie.type_of_enemy = 'Ogre'"
# )
# print("But we try not to encourage this functionality.")

# V4 - Encapsulation
# Bundling of Data
# Change our public attributes to private
# Use double underscore to do that
# Getters and setters in encapsulation help in doing this
# Helps keep related fields and methods together

zombie = Enemy("Zombie", 10, 1)
big_zombie = Enemy("Big Zombie", 100, 10)


print(zombie.get_type_of_enemy())
print(big_zombie.get_type_of_enemy())
