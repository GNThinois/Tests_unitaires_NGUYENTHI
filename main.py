from Module import Person, Wizard, HealthPotion
import numpy as np

user_1 = Person("Hero")
user_2 = Wizard("Wizard")

def fight(fighter1, fighter2):
    while fighter1.is_dead() == False and fighter2.is_dead() == False:
        random = np.random.randint(2)

        if random == 1:
            fighter1.hit(fighter2)
        else:
            fighter2.hit(fighter1)

        random_health_potion_use = np.random.randint(3)

        if random_health_potion_use == 0:
            HealthPotion.was_used_by(user_1)
        elif random_health_potion_use == 1:
            HealthPotion.was_used_by(fighter2)
        else:
            pass

    if fighter1.get_life_points() <= 0:
        print(fighter2.name + " wins")
    if fighter2.get_life_points() <= 0:
        print(fighter1.name + " wins")


fight(user_1, user_2)