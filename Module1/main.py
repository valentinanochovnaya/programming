import journey_class
from validator import *

container = journey_class.JourneyContainer()


def menu_choose_file():
    option = input('Print another file to choose a file or print def for default ')
    if option == 'another':
        print('Enter a file name: ')
        file_name = input()
        return file_name
    else:
        file_name = 'test.txt'
        return file_name


def menu_read_data():
    try:
        file_name = menu_choose_file()
        container.read_from_file(file_name)
        print(container)
        return container
    except AllErrors:
        for i in AllErrors.list_of_custom_erros:
            print(i.message.message)


def menu_add():
    try:
        file_name = menu_choose_file()
        id = input('Enter an id: ')
        Validator.validate_number(Validator.is_exist(container.list_of_elements, id))
        username = input('Enter a username: ')
        Validator.validate_name(Validator.is_name_exists(username, container.list_of_elements))
        budget = Validator.validate_budget(input('Enter a budget: '))
        start_date = Validator.validate_date(input('Enter a start_date: '))
        end_date = Validator.validate_date(input('Enter an end_date: '))
        city = Validator.validate_city(input('Choose a city: Paris, Rome, Naples or Vienna '))
        element = {
            'ID': id, 'username': username, 'budget': budget, 'start_date': start_date, 'end_date': end_date,
            'city': city
        }
        container.add_element(file_name, element)
    except AllErrors:
        for i in AllErrors.list_of_custom_erros:
            print(i.message.message)


def menu_clear():
    container.clear_list()


def menu_exit():
    exit(0)


def menu_budget():
    file_name = 'calculation.txt'
    container.overall_budget(file_name, container.list_of_elements)


def menu():
    menu_options = {'add': menu_add, 'read': menu_read_data, 'clear': menu_clear, 'calculate': menu_budget, 'exit': menu_exit}
    message = ' add \n' \
              ' read \n' \
              ' sort \n' \
              ' clear \n' \
              ' calculate \n' \
              ' exit \n'
    while True:
        print(message)
        option = input('Choose an option to perform: ')
        try:
            if option:
                menu_options[option]()
        except:
            print('Oops, seems that invalid menu option was printed')


menu()
