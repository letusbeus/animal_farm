import view
from user_commands import show_all, add_few_animal, add_command, all_animals, add_new_animal


def start_registry():
    view.welcome()
    while True:
        view.menu_commands()
        program = input(str())
        menu = {
            '1': 'start',
            '2': 'add',
            '5': 'quit',
            '4': 'show_all',
            '3': 'learn_animal'
        }
        try:
            program = menu[program]
            if program == 'quit':
                exit(0)
            elif program == 'start':
                add_few_animal()
                view.animal_added()
                show_all()
            elif program == 'add':
                add_new_animal()
                view.animal_added()
            elif program == 'show_all':
                if len(all_animals) > 0:
                    show_all()
                else:
                    view.empty_farm()
            elif program == 'learn_animal':
                if len(all_animals) == 0:
                    view.empty_farm()
                else:
                    show_all()
                    view.animal_for_command()
                    id_param = int(input())
                    view.command_request()
                    key_type = input()
                    view.command_answer()
                    val_type = input()
                    add_command(id_param, key_type, val_type)
        except KeyError:
            view.menu_error()
