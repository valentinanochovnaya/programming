import freelancer_class
from validator import *

container = freelancer_class.FreelancerContainer()


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
    except InvalidNameError:
        print('Name should not contain numbers')
    except InvalidEmailError:
        print('An invalid email was printed')
    except InvalidPhoneNumberError:
        print('An invalid phone number was printed')
    except ValueError:
        print('An invalid type was printed. Should be a number')
    except NotRecognizablePositionError:
        print('There is not such position')
    except AvailabilityError:
        print('A freelancer cannot work more than 40 hrs per week')
    except FilePathError:
        print('File does not exist')


def menu_add():
    try:
        file_name = menu_choose_file()
        id = input('Enter an id: ')
        Validator.validate_number(Validator.is_exist(container.list_of_elements, id))
        name = Validator.validate_name(input('Enter a name: '))
        email = Validator.validate_email(input('Enter an email: '))
        phone_number = Validator.validate_phone_number(input('Enter a phone number: '))
        availability = Validator.validate_availability(input('Enter an availability: '))
        salary = Validator.validate_number(input('Enter a salary: '))
        position = Validator.validate_position(input('Choose position: BE Developer, FE Developer or DevOps '))
        element = {
            'ID': id, 'name': name, 'email': email, 'phone_number': phone_number, 'availability': availability,
            'salary': salary, 'position': position
        }
        container.add_element(file_name, element)
    except IdAlreadyExistsError:
        print('This id is already in list')
    except InvalidNameError:
        print('Name should not contain numbers')
    except InvalidEmailError:
        print('An invalid email was printed')
    except InvalidPhoneNumberError:
        print('An invalid phone number was printed')
    except ValueError:
        print('An invalid type was printed. Should be a number')
    except NotRecognizablePositionError:
        print('There is not such position')
    except AvailabilityError:
        print('A freelancer cannot work more than 40 hrs per week')
    except FilePathError:
        print('File does not exist')


def menu_remove():
    try:
        id = Validator.validate_number(input('Enter an id: '))
        container.remove_element(id)
    except InvalidNumberError:
        print('An invalid id type was printed')


def menu_sort():
    field = input('Enter a key which should be sorted ')
    result = container.sort(field)
    print(result)


def menu_edit():
    try:
        id = Validator.validate_number(input('Enter an id of element to edit: '))
        changes = []
        while True:
            option = input('Enter next for next changes, enter stop to finish')
            if option == 'stop':
                container.edit_element(id, changes)
                break
            key_ = input("Enter a key to edit: ")
            value = input("Enter a new value for the key: ")
            changes.append(key_ + '=' + value)
    except InvalidNumberError:
        print('An invalid id type was printed')
    except ValueError:
        print('Printed id was not found')


def menu_search():
    value = input('Enter a value that should be found')
    print(container.partial_search(value))


def menu_clear():
    container.clear_list()


def menu_exit():
    exit(0)


def menu():
    menu_options = {'add': menu_add, 'remove': menu_remove, 'change': menu_edit,
                    'search': menu_search, 'read': menu_read_data, 'clear': menu_clear, 'sort': menu_sort, 'exit': menu_exit}
    message = ' add \n' \
              ' remove \n' \
              ' change \n' \
              ' search \n' \
              ' read \n' \
              ' sort \n' \
              ' clear \n' \
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
