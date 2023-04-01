import random
import view
from animals import Animal
from animals_params import *


def show_all():
    for animal in all_animals:
        print(animal)


def add_few_animal():
    view.qty_request()
    qty = int(input())
    for i in range(qty):
        name = random.choice(animal_name)
        a_spec = random.choice(animal_species)
        if a_spec in ("Лошадь", "Верблюд", "Осел"):
            a_type = animal_type[1]
        else:
            a_type = animal_type[0]
        new_animal = Animal(name, a_spec, a_type)
        all_animals.append(new_animal)
    return all_animals


def add_new_animal():
    view.name_request()
    name = input()
    view.animal_select()
    a_spec = int(input())
    if a_spec in (4, 5, 6):
        a_type = animal_type[1]
    else:
        a_type = animal_type[0]
    new_animal = Animal(name, animal_species[a_spec - 1], a_type)
    all_animals.append(new_animal)
    return new_animal


def add_command(anim_id, key, val):
    anim_true = all_animals.pop(anim_id - 1)
    anim_true.set_commands(key, val)
    all_animals.insert(anim_id - 1, anim_true)
    view.command_added(anim_id, key)
