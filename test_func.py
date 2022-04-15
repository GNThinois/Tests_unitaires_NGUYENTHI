from Module import Person, Wizard, HealthPotion

def test_init():
    test_person = Person("Hero")
    #user_test2 = Wizard("Wizard")
    expected_result_1 = 100
    #expected_result_2 = 80
    assert test_person.life_points == expected_result_1
    #assert user_test2.life_points == expected_result_2

def test_name():
    test_person = Person("Test")
    expected_result = "Test"
    assert test_person.name == expected_result

def test_hit():
    test_person = Person("Test1")
    test_wizard = Wizard("Test2")
    expected_result = 85
    test_wizard.hit(test_person)
    assert test_person.life_points == expected_result

def test_is_dead():
    test_person = Person("Test 1")
    test_person.life_points = 0
    expected_result = True
    assert test_person.is_dead() == expected_result

def test_gained_life_points():
    test_person = Person("Test 1")
    test_person.gained_life_points(10)
    expected_result = 110
    assert test_person.life_points == expected_result

def test_get_life_points():
    test_person = Person("Test 1")
    expected_result = 100
    assert test_person.life_points == expected_result

def test_multi_func():
    test_person = Person("Test1")
    #100hp
    test_wizard = Wizard("Test2")
    #80hp
    HealthPotion.was_used_by(test_person)
    #+10
    assert test_person.get_life_points() == 110
    test_wizard.hit(test_person)
    #-15
    assert test_person.get_life_points() == 95
    test_person.gained_life_points(10)
    #+10
    assert test_person.get_life_points() == 105

