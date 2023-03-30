class Animal:
    __id = 0

    def __init__(self, name, animal_species, animal_type, __animal_commands=None):
        if __animal_commands is None:
            __animal_commands = {}
        self.__id = self.__id + 1
        Animal.__id += 1
        self.__name = name
        self.__animal_species = animal_species
        self.__animal_type = animal_type
        self.__animal_commands = __animal_commands

    def __str__(self):
        return f'ID:{self.__id}, Кличка: {self.__name}, Вид: {self.__animal_species}, ' \
               f'Класс животного: {self.__animal_type}, Команды животного: {self.__animal_commands}'

    def set_commands(self, key, val):
        self.__animal_commands[key] = val

    def get_attr(self):
        return self.__id, self.__name, self.__animal_species, self.__animal_type, self.__animal_commands

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__animal_species
