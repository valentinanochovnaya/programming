import freelancer_class
from freelancer_class import *
from validator import Validator


class FileManager:
    @staticmethod
    def read_from_file(file_name):
        file = open(file_name)
        freelancers = []
        freelancer = freelancer_class.Freelancer()
        for line in file:
            if line == '---\n':
                freelancers.append(freelancer)
                freelancer = freelancer_class.Freelancer()
                continue
            line_input = line.split(':')
            freelancer.__setattr__(line_input[0].strip(),
                                   Validator.choose_validate_function(line_input[0].strip(), line_input[1].strip()))

        file.close()
        return freelancers

    @staticmethod
    def add_element(file_name, element):
        file = open(file_name, mode='a')
        string = ''
        for key, value in element.items():
            string += str(key) + ' : ' + str(value) + '\n'
        file.write(string)
        file.write('---\n')
        file.close()
