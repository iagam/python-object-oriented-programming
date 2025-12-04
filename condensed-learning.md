## 🐍 OOP Revision Guide

-----

## 1\. 🏗️ Classes, Attributes, and Constructors

A **Class** is the blueprint for creating objects, defining their attributes (data) and methods (behavior). An **Object** is an instance of a class.

### Constructors (`__init__`)

The `__init__` method is the constructor, which is automatically called when a new object is created (instantiated). It initializes object attributes by assigning values to them.

  * **Your Example (`Enemy`):**
    The constructor takes parameters to set up the object's initial state:
    ```python
    def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int, regeneration_points: int):
        self.__type_of_enemy = type_of_enemy # Set private attribute
        self.health_points = health_points   # Set public attribute
        # ... other attributes ...
    ```
  * **Instantiation Example (from `main.py`):**
    ```python
    ogre = Ogre(20, 3) # Creates an instance of Ogre, calling its constructor.
    ```

### Runtime Type Checking

You implemented **explicit runtime checks** in the constructors of `Enemy` and `Hero`. This is a good practice to ensure data integrity and prevent errors by verifying that required attributes (like `health_points` and `attack_damage`) are of the correct type (integer).

  * **Your Example (from `Hero.py`):**
    ```python
    if not isinstance(health_points, int):
        raise TypeError(
            f"health_points must be an integer, but got {type(health_points).__name__}"
        )
    ```

-----

## 2\. 🛡️ Encapsulation (Information Hiding)

**Encapsulation** is the practice of bundling data (attributes) and methods that operate on that data into a single unit (the class). It helps to keep related fields and methods together.

### Python's Approach (Name Mangling)

In Python, you signal that an attribute should be considered private and not accessed directly from outside the class by using a **double underscore prefix (`__`)**. This triggers name mangling, making the attribute implicitly "private."

  * **Private Attribute Example (from `Enemy.py`):**
    ```python
    self.__type_of_enemy = type_of_enemy 
    ```
  * **Getters (Accessors)**: To safely read the value of a private attribute, you provide a public method called a getter.
      * **Your Getter Example (from `Enemy.py`):**
        ```python
        def get_type_of_enemy(self):
            return self.__type_of_enemy
        ```

-----

## 3\. ➡️ Inheritance (Code Reusability)

**Inheritance** is the process where a new class (child/subclass) acquires properties and behavior from an existing class (parent/superclass). It creates a hierarchy between classes and models the **"Is-A"** relationship.

### The Role of `super()` and `self`

  * **`self`**: Refers to the **current object** being created or instantiated.

  * **`super()`**: Refers to the **parent class**. It's used primarily to call parent class methods or constructors.

  * **Parent Constructor Call Example (from `Zombie.py`):**
    The child class `Zombie` calls the parent's (`Enemy`'s) constructor to initialize the base properties like health and damage:

    ```python
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
    ```

-----

## 4\. 🔄 Method Overriding and Augmentation

**Method Overriding** occurs when a child class implements a method that is already present in its parent class.

  * **Overriding for Unique Behavior**:
    The child class provides its own specialized implementation, completely replacing the parent's behavior for that method.
      * **Your Example (from `Zombie.py`):**
        The `Zombie`'s **`talk()`** method completely replaces the generic `Enemy`'s `talk()` method:
        ```python
        # augmenting parent method
        def talk(self):
            print('*Grumbling...*')
        ```
  * **New Methods**: Child classes can also introduce entirely new, specialized methods not found in the parent.
      * **Your Example (from `Zombie.py`):**
        ```python
        def spread_disease(self):
            # ... unique zombie behavior ...
        ```

-----

## 5\. 🎭 Polymorphism (Flexibility in Design)

**Polymorphism** means "many forms". In OOP, it refers to the ability of different objects (from different classes) to respond to the **same method call** in their own unique way.

### Polymorphism in Action

Your `main.py` demonstrates this pillar beautifully:

1.  **Shared Interface**: All objects (`Ogre`, `Enemy`, `Zombie`) have a `talk()` method (due to inheritance and overriding).
2.  **Generic Collection**: They are stored in a heterogeneous list:
    ```python
    enemies_in_the_area = [ogre, skeleton, zombie_a, zombie_b]
    ```
3.  **Dynamic Execution (Dispatch)**: The loop calls the same method (`enemy.talk()`), but the output is tailored based on the actual object's type at runtime.

<!-- end list -->

  * **Code Example (from `main.py`):**
    ```python
    for enemy in enemies_in_the_area:
        print(f"Object Type: {enemy.get_type_of_enemy()}")
        enemy.talk() # This calls Zombie.talk(), Ogre.talk(), or Enemy.talk() appropriately
    ```

-----

## 6\. 🛠️ Association (The "Has-A" Relationship)

**Association** describes how objects relate to each other, often modeling a **"Has-A"** relationship (e.g., A `Hero` **has a** `Weapon`).

  * **Aggregation/Composition**: This is implemented by one class holding an instance of another class as an attribute.

  * **Your Example (`Hero` and `Weapon`):**
    The `Hero` class maintains a reference to a `Weapon` object. When the `Hero` equips the weapon, it accesses the `Weapon`'s properties (`attack_increase`) to modify its own base attack damage.

    ```python
    # In Hero:
    self.weapon: Weapon = None 
    # ...
    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            # Uses the Weapon's attribute to augment the Hero's attack_damage
            self.attack_damage+=self.weapon.attack_increase 
            self.is_weapon_equipped = True
    ```
