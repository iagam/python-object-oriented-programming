# V1 - Introduction to OOP - Create an enemy class
# class Enemy:

#     type_of_enemy: str
#     health_points: int = 10
#     attack_damage: int = 1

# V2 - Abstraction
# Abstarction means to hide implementation and only show necessary details to the user.
# User doesn't need to know what's going under the hood.
# In the long run helps make code scalable
# Propoagates the DRY (Don't Repeat Yourself) principle

class Enemy:

    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight.")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")
