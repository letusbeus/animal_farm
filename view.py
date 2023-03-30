from animals import Animal
from animals_params import all_animals


def welcome():
    print('\n*** Добро пожаловать в Реестр домашних животных! ***')


def menu_commands():
    print('''--------------- Выберите опцию: ---------------
1 - Добавить в реестр несколько животных
2 - Добавить в реестр одно животное
3 - Обучить животное команде
4 - Показать всех животных
5 - Завершить работу
Вводите сюда --->: ''', end=''
          )


def qty_request():
    print('Сколько животных вы желаете внести в реестр?')


def name_request():
    print('Введите кличку животного: ')


def animal_select():
    print('''Введите тип животного, которое вы хотите добавить:
1 - Кот
2 - Собака
3 - Хомяк
4 - Лошадь
5 - Верблюд
6 - Осел
Вводите сюда --->: ''', end=''
          )


def animal_added():
    print('Животное(ые) добавлено(ы) успешно!')


def empty_farm():
    print('Реестр пуст')


def menu_error():
    print('Введено неверное значение, возврат к выбору опции')


def animal_for_command():
    print('Введите ID животного, которое вы хотите обучить новой команде: ')


def command_request():
    print('Введите название команды:')


def command_answer():
    print('Опишите совершаемое действие:')


def command_added(anim_id, key):
    print(f'{Animal.get_species(all_animals[anim_id - 1])} по кличке '
          f'{Animal.get_name(all_animals[anim_id - 1])} (ID: {anim_id}) обучен(а) новой команде: {key}')
