from validator import Validator
from file_manager import FileManager


class Freelancer:

    def __init__(self, ID=None, name=None, email=None, phone_number=None, availability=None, salary=None,
                 position=None):
        self.ID = ID
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.availability = availability
        self.salary = salary
        self.position = position

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
        self.list_of_elements.append(value)

    def read_from_file(self, file_name):
        freelancers = FileManager.read_from_file(file_name)
        for element in freelancers:
            self.list_of_elements.append(element)

    def add_element(self, file_name, element):
        FileManager.add_element(file_name, element)
        self.append(Freelancer(element))

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
