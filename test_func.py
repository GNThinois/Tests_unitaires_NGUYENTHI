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
