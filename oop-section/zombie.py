from enemy import *
import random

# Zombie as a child class of Enemy
class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        # Call Parent constructors using super
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
            regeneration_points=2,
        )

    # augmenting parent method
    def talk(self):
        print('*Grumbling...*')

    # adding new methods
    def spread_disease(self):
        enemy_type = self.get_type_of_enemy()
        print(f'{enemy_type} is trying to spread diseases.')

    def special_attack(self):
        enemy_type = self.get_type_of_enemy()
        did_special_attack_work = random.random()
        if did_special_attack_work < 0.5:
            self.health_points += self.regeneration_points
            print(f"{enemy_type} generated {self.regeneration_points} HP")
