# V1 - Introduction to OOP - Create an enemy class
# class Enemy:

#     type_of_enemy: str
#     health_points: int = 10
#     attack_damage: int = 1

# ---------------------------------------------------------------------------------------------

# V2 - Abstraction
# Abstarction means to hide implementation and only show necessary details to the user.
# User doesn't need to know what's going under the hood.
# In the long run helps make code scalable
# Propoagates the DRY (Don't Repeat Yourself) principle

# class Enemy:

#     type_of_enemy: str
#     health_points: int = 10
#     attack_damage: int = 1

#     def talk(self):
#         print(f"I am a {self.type_of_enemy}. Be prepared to fight.")

#     def walk_forward(self):
#         print(f"{self.type_of_enemy} moves closer to you.")

#     def attack(self):
#         print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")

# ---------------------------------------------------------------------------------------------

# V3 - Constructors
# 1. Default/Empty Constructors
# 2. No Arguments Constructors
# 3. Parameter Constructors

# class Enemy:

#     # Add parameter constructor class
#     def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int):
#         self.type_of_enemy = type_of_enemy

#         # Explicit Runtime Check
#         if not isinstance(health_points, int):
#             raise TypeError(
#                 f"health_points must be an integer, but got {type(health_points).__name__}"
#             )
#         self.health_points = health_points

#         # Explicit Runtime Check
#         if not isinstance(attack_damage, int):
#             raise TypeError(
#                 f"attack_damage must be an integer, but got {type(attack_damage).__name__}"
#             )
#         self.attack_damage = attack_damage

#     def talk(self):
#         print(f"I am a {self.type_of_enemy}. Be prepared to fight.")

#     def walk_forward(self):
#         print(f"{self.type_of_enemy} moves closer to you.")

#     def attack(self):
#         print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")

# ---------------------------------------------------------------------------------------------

# V4 - Encapsulation
# Bundling of Data
# Change our public attributes to private
# Use double underscore to do that
# Getters and setters in encapsulation help in doing this
# Helps keep related fields and methods together


class Enemy:

    # Add parameter constructor class
    def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int):
        self.__type_of_enemy = type_of_enemy

        # Explicit Runtime Check
        if not isinstance(health_points, int):
            raise TypeError(
                f"health_points must be an integer, but got {type(health_points).__name__}"
            )
        self.health_points = health_points

        # Explicit Runtime Check
        if not isinstance(attack_damage, int):
            raise TypeError(
                f"attack_damage must be an integer, but got {type(attack_damage).__name__}"
            )
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight.")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage.")

    def get_type_of_enemy(self):
        return self.__type_of_enemy
