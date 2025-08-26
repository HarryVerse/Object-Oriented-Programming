import thor_superhero

def test_thor_initialization():
    """Test Thor class initialization"""
    print("Testing Thor initialization...")
    thor = thor_superhero.Thor()
    assert thor.name == "Thor"
    assert thor.secret_identity == "Thor Odinson"
    assert thor.origin == "Asgard"
    assert thor.hammer_name == "Mjolnir"
    assert thor.is_worthy == True
    assert thor.power_level == 950
    assert thor.lightning_power == 100
    print("✓ Thor initialization test passed")

def test_thor_custom_initialization():
    """Test Thor with custom parameters"""
    print("Testing Thor custom initialization...")
    thor = thor_superhero.Thor(
        secret_identity="God of Thunder",
        origin="Midgard",
        hammer_name="Stormbreaker",
        is_worthy=False
    )
    assert thor.secret_identity == "God of Thunder"
    assert thor.origin == "Midgard"
    assert thor.hammer_name == "Stormbreaker"
    assert thor.is_worthy == False
    print("✓ Thor custom initialization test passed")

def test_thor_methods_worthy():
    """Test Thor methods when worthy"""
    print("Testing Thor methods (worthy state)...")
    thor = thor_superhero.Thor()
    
    # Test introduce
    intro = thor.introduce()
    assert "Thor" in intro and "Thor Odinson" in intro and "Asgard" in intro
    
    # Test string representation
    str_repr = str(thor)
    assert "Thor" in str_repr and "950" in str_repr
    
    # Test attack
    attack_result = thor.attack("Loki")
    assert "attacks Loki" in attack_result and "Mjolnir" in attack_result
    
    # Test summon lightning
    lightning_result = thor.summon_lightning()
    assert "summons lightning" in lightning_result and "Mjolnir" in lightning_result
    assert thor.lightning_power == 90  # Should decrease by 10
    
    # Test use_power (polymorphism)
    power_result = thor.use_power()
    assert "summons lightning" in power_result
    
    # Test check_worthiness
    worthiness = thor.check_worthiness()
    assert "worthy" in worthiness.lower()
    
    print("✓ Thor methods (worthy) test passed")

def test_thor_methods_unworthy():
    """Test Thor methods when unworthy"""
    print("Testing Thor methods (unworthy state)...")
    thor = thor_superhero.Thor(is_worthy=False)
    
    # Test attack when unworthy
    attack_result = thor.attack("Thanos")
    assert "cannot lift" in attack_result or "not worthy" in attack_result
    
    # Test summon lightning when unworthy
    lightning_result = thor.summon_lightning()
    assert "not worthy" in lightning_result.lower()
    
    # Test check_worthiness
    worthiness = thor.check_worthiness()
    assert "unworthy" in worthiness.lower()
    
    print("✓ Thor methods (unworthy) test passed")

def test_worthiness_transitions():
    """Test Thor's worthiness state transitions"""
    print("Testing worthiness transitions...")
    thor = thor_superhero.Thor()
    
    # Become unworthy
    unworthy_msg = thor.become_unworthy()
    assert "unworthy" in unworthy_msg.lower()
    assert thor.is_worthy == False
    
    # Become worthy again
    worthy_msg = thor.become_worthy()
    assert "worthy" in worthy_msg.lower()
    assert thor.is_worthy == True
    
    print("✓ Worthiness transitions test passed")

def test_polymorphism_animals():
    """Test polymorphism with animal classes"""
    print("Testing animal polymorphism...")
    
    animals = [
        thor_superhero.Eagle("Thunderwing"),
        thor_superhero.Shark("Deep Blue"),
        thor_superhero.Cheetah("Speedy")
    ]
    
    for animal in animals:
        move_result = animal.move()
        assert animal.name in move_result
        # Check for movement type indicators
        if isinstance(animal, thor_superhero.Eagle):
            assert "soars" in move_result or "sky" in move_result
        elif isinstance(animal, thor_superhero.Shark):
            assert "swims" in move_result or "ocean" in move_result
        elif isinstance(animal, thor_superhero.Cheetah):
            assert "runs" in move_result or "speed" in move_result
    
    print("✓ Animal polymorphism test passed")

def test_polymorphism_vehicles():
    """Test polymorphism with vehicle classes"""
    print("Testing vehicle polymorphism...")
    
    vehicles = [
        thor_superhero.Car("Lightning"),
        thor_superhero.Plane("Sky King"),
        thor_superhero.Boat("Sea Serpent")
    ]
    
    for vehicle in vehicles:
        move_result = vehicle.move()
        assert vehicle.name in move_result
        # Check for movement type indicators
        if isinstance(vehicle, thor_superhero.Car):
            assert "drives" in move_result or "road" in move_result
        elif isinstance(vehicle, thor_superhero.Plane):
            assert "flies" in move_result or "air" in move_result
        elif isinstance(vehicle, thor_superhero.Boat):
            assert "sails" in move_result or "water" in move_result
    
    print("✓ Vehicle polymorphism test passed")

def test_inheritance_hierarchy():
    """Test inheritance relationships"""
    print("Testing inheritance hierarchy...")
    
    # Test Thor inherits from Superhero
    thor = thor_superhero.Thor()
    assert isinstance(thor, thor_superhero.Superhero)
    
    # Test animal inheritance
    eagle = thor_superhero.Eagle("Test")
    assert isinstance(eagle, thor_superhero.Animal)
    
    # Test vehicle inheritance
    car = thor_superhero.Car("Test")
    assert isinstance(car, thor_superhero.Vehicle)
    
    print("✓ Inheritance hierarchy test passed")

def run_all_tests():
    """Run all test functions"""
    print("=" * 60)
    print("COMPREHENSIVE TESTING - THOR SUPERHERO PROGRAM")
    print("=" * 60)
    
    try:
        test_thor_initialization()
        test_thor_custom_initialization()
        test_thor_methods_worthy()
        test_thor_methods_unworthy()
        test_worthiness_transitions()
        test_polymorphism_animals()
        test_polymorphism_vehicles()
        test_inheritance_hierarchy()
        
        print("=" * 60)
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        return False

if __name__ == "__main__":
    run_all_tests()
