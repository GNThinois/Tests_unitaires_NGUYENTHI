from Module import Person, Wizard, HealthPotion

def test_init():
    user_test1 = Person("Hero")
    expected_result = 100
    assert user_test1.life_points == expected_result

def test_name():
    user_test2 = Person("Test")
    expected_result = "Test"
    assert user_test2.name == expected_result