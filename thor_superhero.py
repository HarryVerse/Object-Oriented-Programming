class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, secret_identity, origin):
        self.name = name
        self.secret_identity = secret_identity
        self.origin = origin
        self.power_level = 100
    
    def introduce(self):
        """Introduce the superhero"""
        return f"I am {self.name}, also known as {self.secret_identity} from {self.origin}"
    
    def use_power(self):
        """Base power usage method - to be overridden by subclasses"""
        return f"{self.name} uses a generic power!"
    
    def __str__(self):
        return f"{self.name} (Power Level: {self.power_level})"


class Thor(Superhero):
    """Thor class inheriting from Superhero"""
    
    def __init__(self, secret_identity="Thor Odinson", origin="Asgard", hammer_name="Mjolnir", is_worthy=True):
        super().__init__("Thor", secret_identity, origin)
        self.hammer_name = hammer_name
        self.is_worthy = is_worthy
        self.power_level = 950  # Thor is very powerful!
        self.lightning_power = 100
    
    def summon_lightning(self):
        """Thor's signature lightning power"""
        if self.is_worthy:
            self.lightning_power -= 10
            return f"⚡ {self.name} summons lightning with {self.hammer_name}! ⚡"
        else:
            return f"{self.name} is not worthy to summon lightning!"
    
    def attack(self, target):
        """Attack with hammer"""
        if self.is_worthy:
            return f"🔨 {self.name} attacks {target} with {self.hammer_name}!"
        else:
            return f"{self.name} cannot lift {self.hammer_name} - not worthy!"
    
    def use_power(self):
        """Override the base power usage method"""
        return self.summon_lightning()
    
    def become_unworthy(self):
        """Make Thor unworthy (for dramatic effect)"""
        self.is_worthy = False
        return f"{self.name} has become unworthy! {self.hammer_name} cannot be lifted."
    
    def become_worthy(self):
        """Make Thor worthy again"""
        self.is_worthy = True
        return f"{self.name} is worthy again! {self.hammer_name} answers the call!"
    
    def check_worthiness(self):
        """Check if Thor is worthy"""
        status = "worthy" if self.is_worthy else "unworthy"
        return f"{self.name} is {status} to wield {self.hammer_name}"


# Polymorphism Challenge - Animal/Vehicle classes
class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Base move method - to be overridden"""
        return f"{self.name} moves in a generic way"


class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Base move method - to be overridden"""
        return f"{self.name} moves in a generic way"


# Specific animal classes
class Eagle(Animal):
    def move(self):
        return f"🦅 {self.name} soars through the sky! Flying high above the clouds."


class Shark(Animal):
    def move(self):
        return f"🦈 {self.name} swims powerfully through the ocean depths."


class Cheetah(Animal):
    def move(self):
        return f"🐆 {self.name} runs at incredible speed across the savannah!"


# Specific vehicle classes
class Car(Vehicle):
    def move(self):
        return f"🚗 {self.name} drives smoothly on the road. Vroom vroom!"


class Plane(Vehicle):
    def move(self):
        return f"✈️ {self.name} flies through the air at high altitude."


class Boat(Vehicle):
    def move(self):
        return f"⛵ {self.name} sails across the water with the wind."


def demonstrate_polymorphism(objects):
    """Demonstrate polymorphism by calling move() on different objects"""
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION")
    print("="*50)
    
    for obj in objects:
        print(obj.move())
        print("-" * 30)


# Main demonstration function
def main():
    print("THOR SUPERHERO DEMONSTRATION")
    print("="*50)
    
    # Create Thor instance
    thor = Thor(secret_identity="Thor Odinson", origin="Asgard", hammer_name="Mjolnir")
    
    # Demonstrate Thor's capabilities
    print(thor.introduce())
    print(thor)
    print(thor.check_worthiness())
    print(thor.attack("Loki"))
    print(thor.summon_lightning())
    print(thor.use_power())  # Polymorphism in action
    
    # Demonstrate worthiness change
    print("\n" + "-"*50)
    print(thor.become_unworthy())
    print(thor.attack("Thanos"))  # Should fail
    print(thor.summon_lightning())  # Should fail
    
    print("\n" + "-"*50)
    print(thor.become_worthy())
    print(thor.attack("Thanos"))  # Should work again
    print(thor.summon_lightning())  # Should work again
    
    # Polymorphism demonstration with animals and vehicles
    animals_vehicles = [
        Eagle("Thunderbird"),
        Shark("Jaws"),
        Cheetah("Flash"),
        Car("Lightning McQueen"),
        Plane("Sky King"),
        Boat("Sea Serpent")
    ]
    
    demonstrate_polymorphism(animals_vehicles)


if __name__ == "__main__":
    main()
