# OOP Concepts Demonstration with Thor and Polymorphism

This Python project demonstrates Object-Oriented Programming (OOP) concepts using Thor from Marvel as the main example, along with a polymorphism challenge featuring animals and vehicles.

## 🎯 Project Overview

The project consists of two main activities:

1. **Thor Superhero Class**: A comprehensive class hierarchy showcasing inheritance, encapsulation, and method overriding
2. **Polymorphism Challenge**: Multiple classes with the same `move()` method but different implementations

## 🏗️ OOP Concepts Demonstrated

### 1. Inheritance
- `Superhero` base class with common attributes and methods
- `Thor` subclass that inherits from `Superhero` and adds specific functionality
- Animal and Vehicle base classes with specialized subclasses

### 2. Polymorphism
- Different classes implementing the same `move()` method differently
- Method overriding in the inheritance hierarchy
- Runtime method resolution

### 3. Encapsulation
- Private attributes with controlled access through methods
- State management (worthiness, power levels)
- Controlled state transitions

## 📁 File Structure

```
.
├── thor_superhero.py    # Main program with all classes and demonstration
├── test_thor_program.py # Comprehensive test suite
├── README.md           # This file
```

## 🚀 How to Run

### Run the main demonstration:
```bash
python thor_superhero.py
```

### Run comprehensive tests:
```bash
python test_thor_program.py
```

## 🦸♂️ Thor Class Features

### Attributes:
- `name`: "Thor" (inherited from Superhero)
- `secret_identity`: "Thor Odinson" or custom
- `origin`: "Asgard" or custom
- `hammer_name`: "Mjolnir" or custom
- `is_worthy`: Boolean indicating if Thor can wield his hammer
- `power_level`: Numeric power rating (950 for Thor)
- `lightning_power`: Specific lightning ability resource

### Methods:
- `summon_lightning()`: Thor's signature power (consumes lightning_power)
- `attack(target)`: Attack with hammer (requires worthiness)
- `become_unworthy()`: Dramatic state change
- `become_worthy()`: Restore worthiness
- `check_worthiness()`: Check current state
- `use_power()`: Overridden from Superhero base class

## 🎭 Polymorphism Challenge

### Animal Classes:
- **Eagle**: `move()` returns "🦅 {name} soars through the sky!"
- **Shark**: `move()` returns "🦈 {name} swims powerfully through the ocean!"
- **Cheetah**: `move()` returns "🐆 {name} runs at incredible speed!"

### Vehicle Classes:
- **Car**: `move()` returns "🚗 {name} drives smoothly on the road!"
- **Plane**: `move()` returns "✈️ {name} flies through the air!"
- **Boat**: `move()` returns "⛵ {name} sails across the water!"

## 🧪 Testing

The project includes a comprehensive test suite that covers:
- Class initialization with default and custom parameters
- Method functionality in different states (worthy/unworthy)
- Inheritance relationships and hierarchy
- Polymorphism across different object types
- Edge cases and state transitions

## 💡 Key Learning Points

1. **Inheritance**: Creating base classes and specialized subclasses
2. **Polymorphism**: Same method name, different implementations
3. **Encapsulation**: Controlled access to object state
4. **Method Overriding**: Subclasses providing specific implementations
5. **Class Design**: Thoughtful attribute and method organization

## 🛠️ Technical Details

- **Python Version**: 3.6+
- **Dependencies**: None (pure Python)
- **Design Patterns**: Inheritance, Polymorphism, Encapsulation

## 📚 Example Usage

```python
from thor_superhero import Thor, Eagle, Car

# Create Thor instance
thor = Thor(secret_identity="God of Thunder", hammer_name="Stormbreaker")
print(thor.attack("Loki"))  # "🔨 Thor attacks Loki with Stormbreaker!"

# Demonstrate polymorphism
objects = [Eagle("Thunderbird"), Car("Sports Car")]
for obj in objects:
    print(obj.move())  # Different output for each class
```

## 🎓 Educational Value

This project serves as an excellent learning tool for understanding:
- Object-Oriented Programming principles
- Class design and hierarchy
- Python class syntax and features
- Practical implementation of OOP concepts
- Testing object-oriented code

## 🤝 Contributing

Feel free to extend this project by:
- Adding more superhero classes
- Creating additional animal/vehicle types
- Implementing more complex inheritance hierarchies
- Adding error handling and validation
- Creating GUI or web interfaces

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed for learning OOP concepts.
