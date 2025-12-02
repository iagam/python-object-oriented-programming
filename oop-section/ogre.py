from enemy import *
import random

class Ogre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
            regeneration_points=3,
        )

    def talk(self):
        enemy_type = self.get_type_of_enemy()
        print(f"{enemy_type} is flapping hands all around")

    def special_attack(self):
        did_special_attack_work = random.random()
        if did_special_attack_work < 0.2:
            self.health_points += self.regeneration_points
            print(
                f"{self.get_type_of_enemy()} gets angry and increses attack by {self.regeneration_points} HP"
            )
