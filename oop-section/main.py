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
# Polymorphism means "many forms." In object-oriented programming (OOP) like Python,
# it refers to the ability of different objects (from different classes) to respond
# to the same method call in their own unique way.
# In our enemy example, this means:
# We can have a list of various enemy objects (Zombie, Enemy, etc.).
# We can loop through the list and call the same method, like talk(), on each object.
# Each object will execute its own version of the talk() method.

# Create instances of different classes
# ogre = Ogre(100, 10)
# skeleton = Enemy("Skeleton", 15, 3)
# zombie_a = Zombie(health_points=10, attack_damage=1)
# zombie_b = Zombie(health_points=12, attack_damage=1)

# # Create a list of heterogeneous objects
# enemies_in_the_area = [ogre, skeleton, zombie_a, zombie_b]

# print("--- Calling the same 'talk()' method on different objects ---")

# # Iterate over the list and call talk() on each object
# for enemy in enemies_in_the_area:
#     print(f"Object Type: {enemy.get_type_of_enemy()}")
#     enemy.talk()
#     print("-" * 10)


# Battle Functiom
def battle(e1: Enemy, e2: Enemy):

    print(
        f"{e1.get_type_of_enemy()} and {e2.get_type_of_enemy()} are ready for battle!"
    )
    print("-" * 30)

    e1.talk()
    e2.talk()
    print("-" * 30)

    while e1.health_points > 0 and e2.health_points > 0:
        print("-" * 10)
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} generated {e1.regeneration_points} HP")
        print(f"{e2.get_type_of_enemy()} generated {e2.regeneration_points} HP")

        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print("-" * 10)
    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins.")
    else:
        print(f"{e1.get_type_of_enemy()} wins.")


zombie = Zombie(20, 2)
ogre = Ogre(15, 4)

battle(zombie, ogre)
