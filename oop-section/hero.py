from weapon import *

class Hero:

    # Add parameter constructor class
    def __init__(
        self,
        health_points: int,
        attack_damage: int
    ):

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
        self.is_weapon_equipped: bool = False
        self.weapon: Weapon = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage+=self.weapon.attack_increase
            self.is_weapon_equipped = True

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} HP damage")