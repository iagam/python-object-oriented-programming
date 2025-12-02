from enemy import *

class Ogre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        enemy_type = self.get_type_of_enemy()
        print(f"{enemy_type} is flapping hands all around")