import journey_class
from validator import Validator
from custom_exeptions import AllErrors


class FileManager:
    @staticmethod
    def read_from_file(file_name):
        file = open(file_name)
        journeys = []
        journey = journey_class.Journey()
        for line in file:
            if line == '---\n':
                journeys.append(journey)
                journey = journey_class.Journey()
                continue
            line_input = line.split(':')
            journey.__setattr__(line_input[0].strip(),
                                Validator.choose_validate_function(line_input[0].strip(), line_input[1].strip()))

        file.close()
        if AllErrors.list_of_custom_erros:
            raise AllErrors()
        else:
            return journeys

    @staticmethod
    def add_element(file_name, element):
        file = open(file_name, mode='a')
        string = ''
        for key, value in element.items():
            string += str(key) + ' : ' + str(value) + '\n'
        file.write(string)
        file.write('---\n')
        file.close()
