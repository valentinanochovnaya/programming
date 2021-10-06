import re
import os
from custom_exeptions import *


class Validator:
    def __init__(self):
        pass

    @classmethod
    def choose_validate_function(cls, key_, value):
        if key_ == 'ID' or key_ == 'salary':
            return cls.validate_number(value)
        elif key_ == 'name':
            return cls.validate_name(value)
        elif key_ == 'email':
            return cls.validate_email(value)
        elif key_ == 'availability':
            return cls.validate_availability(value)
        elif key_ == 'position':
            return cls.validate_position(value)
        elif key_ == 'phone_number':
            return cls.validate_phone_number(value)
        else:
            raise ValueError('Unexpected key')

    @staticmethod
    def validate_number(value):
        number_str = str(value)
        if not number_str.isnumeric():
            raise ValueError()
        return int(number_str)

    @staticmethod
    def validate_phone_number(phone_number):
        phone_number_length = len(phone_number)
        code = '+380'
        is_valid = False
        if code in phone_number:
            is_valid = True
        if phone_number_length == 11:
            is_valid = True
        if is_valid:
            return phone_number
        else:
            raise InvalidPhoneNumberError()

    @staticmethod
    def validate_email(email):
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            raise InvalidEmailError()
        return email

    @staticmethod
    def validate_position(position):
        position_list = ['BE Developer', 'FE Developer', 'DevOps']
        if position in position_list:
            return position
        else:
            raise NotRecognizablePositionError()

    @staticmethod
    def validate_name(name):
        if any(char.isdigit() for char in name):
            raise InvalidNameError()
        return name

    @staticmethod
    def validate_availability(availability):
        all_hrs = 40
        if int(availability) > all_hrs:
            raise AvailabilityError()
        else:
            return availability

    @staticmethod
    def validate_file_path(path):
        if not os.path.exists(str(path)):
            raise FilePathError()
        return path

    @staticmethod
    def is_exist(list_of_elements, id):
        for element in list_of_elements:
            if element.ID == int(id):
                raise IdAlreadyExistsError()
        return int(id)
