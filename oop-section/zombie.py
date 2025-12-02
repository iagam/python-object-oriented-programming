from enemy import *

# Zombie as a child class of Enemy
class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        # Call Parent constructors using super
        super().__init__(type_of_enemy = "Zombie",
                         health_points = health_points,
                         attack_damage = attack_damage)

    # augmenting parent method
    def talk(self):
        print('*Grumbling...*')

    # adding new methods
    def spread_disease(self):
        enemy_type = self.get_type_of_enemy()
        print(f'{enemy_type} is trying to spread diseases.')