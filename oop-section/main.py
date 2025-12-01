from enemy import *

# V1 - Introduction to OOP - Instantiating Enemy Object
enemy = Enemy()
enemy.type_of_enemy = "Zombie"
print(f"{enemy.type_of_enemy} has {enemy.health_points} and {enemy.attack_damage} attack damage")
