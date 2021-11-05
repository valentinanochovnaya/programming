from validator import Validator
from file_manager import FileManager


class Journey:

    def __init__(self, ID=None, username=None, budget=None, start_date=None, end_date=None, city=None):
        self.ID = ID
        self.username = username
        self.budget = budget
        self.start_date = start_date
        self.end_date = end_date
        self.city = city

    def __str__(self):
        journey = "\n"
        for key, value in self.__dict__.items():
            journey += key + " : " + str(value) + "\n"
        return journey

    def __repr__(self):
        journey = "\n"
        for key, value in self.__dict__.items():
            journey += str(value) + "\n"
        return journey


class JourneyContainer:
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
        journeys = FileManager.read_from_file(file_name)
        for element in journeys:
            self.list_of_elements.append(element)

    def add_element(self, file_name, element):
        FileManager.add_element(file_name, element)
        self.append(Journey(element))

    @staticmethod
    def element_to_dict(element):
        return element.__dict__

    def sort(self, field):
        sorted_list = sorted(self.list_of_elements,
                             key=lambda x: x.__dict__[field] if isinstance(x.__dict__[field], int) else x.__dict__[field].lower())
        return sorted_list

    def clear_list(self):
        self.list_of_elements.clear()

    def overall_budget(self, file_name, list_of_elements):
        paris, rome, naples, vienna = 0., 0., 0., 0.
        for element in list_of_elements:
            if element.city == 'Paris':
                paris += element.budget
            elif element.city == 'Rome':
                rome += element.budget
            elif element.city == 'Naples':
                naples += element.budget
            elif element.city == 'Vienna':
                vienna += element.budget
        budgets = { 'paris': paris, 'rome': rome, 'vienna': vienna, 'naples': naples}
        sorted_list = sorted(budgets.items(), key=lambda x: x[1], reverse=True)
        file = open(file_name, mode='a')
        string = ''
        for key, value in budgets.items():
            string += str(key) + ' : ' + str(value) + '\n'
        file.write(string)
        file.write('---\n')
        file.close()


