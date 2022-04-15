import main
from Module import Person, Wizard, HealthPotion
import numpy as np

def test_init():
    user_test1 = Person("Hero")
    expected_result = 80
    assert user_test1.life_points == expected_result

print('tests finis .')