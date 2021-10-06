from validator import Validator
from operator import itemgetter


class Freelancer:

    def __init__(self, ID=None, name=None, email=None, phone_number=None, availability=None, salary=None,
                 position=None):
        self.ID = None if ID is None else Validator.validate_number(ID)
        self.name = None if name is None else Validator.validate_name(name)
        self.email = None if email is None else Validator.validate_email(email)
        self.phone_number = None if phone_number is None else Validator.validate_phone_number(phone_number)
        self.availability = None if availability is None else Validator.validate_availability(availability)
        self.salary = None if salary is None else Validator.validate_number(salary)
        self.position = None if position is None else Validator.validate_position(position)

    def __str__(self):
        freelancer = "\n"
        for key, value in self.__dict__.items():
            freelancer += key + " : " + str(value) + "\n"
        return freelancer

    def __repr__(self):
        freelancer = "\n"
        for key, value in self.__dict__.items():
            freelancer += str(value) + "\n"
        return freelancer


class FreelancerContainer:
    list_of_elements = []
    list_of_ids = []

    def __init__(self):
        pass

    def __str__(self):
        s = ''
        for i in self.list_of_elements:
            s += str(i) + '\n'
        return s

    def __getitem__(self, item):
        return self.list_of_elements[item]

    def append(self, value):
        if not isinstance(value, Freelancer):
            return
        self.append_id(value.ID)
        self.list_of_elements.append(value)

    def append_id(self, ID):
        ID = int(ID)
        if ID in self.list_of_ids:
            return
        self.list_of_ids.append(ID)

    def read_from_file(self, file_name):
        self.list_of_ids.clear()
        self.list_of_elements.clear()
        file = open(file_name)
        freelancer = Freelancer()
        for line in file:
            if line == '---\n':
                self.list_of_elements.append(freelancer)
                freelancer = Freelancer()
                continue
            line_input = line.split(':')
            freelancer.__setattr__(line_input[0].strip(),
                                   Validator.choose_validate_function(line_input[0].strip(), line_input[1].strip()))
            if line_input[0].strip() == 'ID':
                self.append_id(line_input[1].strip())
        file.close()

    def add_element(self, file_name, element):
        file = open(file_name, mode='a')
        string = ''
        for key, value in element.items():
            string += str(key) + ' : ' + str(value) + '\n'
        file.write(string)
        file.write('---\n')
        file.close()
        self.append(element)

    @staticmethod
    def element_to_dict(element):
        return element.__dict__

    def partial_search(self, value):
        result = []
        value_str = str(value)
        for i in self.list_of_elements:
            element_dict = self.element_to_dict(i)
            for key, value in element_dict.items():
                if value_str in str(value):
                    result.append(i)
                    break
        return result

    def remove_element(self, id):
        for i in self.list_of_elements:
            if i.ID == id:
                self.list_of_elements.remove(i)
                break
        return

    def edit_element(self, id, changes):
        is_id = False
        for i in self.list_of_elements:
            if i.ID == id:
                is_id = True
                for change in changes:
                    change_list = change.split('=')
                    i.__setattr__(change_list[0].strip(),
                                  Validator.choose_validate_function(change_list[0].strip(), change_list[1].strip()))
                return
        if not is_id:
            raise ValueError("There is not such an id")

    def sort(self, field):
        sorted_list = sorted(self.list_of_elements,
                             key=lambda x: x.__dict__[field] if isinstance(x.__dict__[field], int) else x.__dict__[field].lower())
        return sorted_list

    def clear_list(self):
        self.list_of_elements.clear()
        self.list_of_ids.clear()
