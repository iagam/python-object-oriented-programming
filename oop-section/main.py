from enemy import *

# V1 - Introduction to OOP - Instantiating Enemy Object
# enemy = Enemy()
# enemy.type_of_enemy = "Zombie"
# print(f"{enemy.type_of_enemy} has {enemy.health_points} and {enemy.attack_damage} attack damage")

# V2 - Abstraction
# Abstarction means to hide implementation and only show necessary details to the user.
# User doesn't need to know what's going under the hood.

zombie = Enemy()
zombie.type_of_enemy = "Zombie"
print(zombie.talk())
print(zombie.walk_forward())
print(zombie.attack())
