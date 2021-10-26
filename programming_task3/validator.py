import re
import os
from custom_exeptions import *


class Validator:
    def __init__(self):
        pass

    @classmethod
    def choose_validate_function(cls, key_, value_):
        validate_dict = {
            'ID': cls.validate_number,
            'name': cls.validate_name,
            'email': cls.validate_email,
            'availability': cls.validate_availability,
            'phone_number': cls.validate_phone_number,
            'salary': cls.validate_number,
            'position': cls.validate_position
        }

        for key, value in validate_dict.items():
            if key == key_:
                return validate_dict[key_](value_)

    @staticmethod
    def validate_number(value):
        number_str = str(value)
        if not number_str.isnumeric():
            return AllErrors().collect_error('number')
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
            return AllErrors().collect_error('phone')

    @staticmethod
    def validate_email(email):
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            return AllErrors().collect_error('email')
        return email

    @staticmethod
    def validate_position(position):
        position_list = ['BE Developer', 'FE Developer', 'DevOps']
        if position in position_list:
            return position
        else:
            return AllErrors().collect_error('position')

    @staticmethod
    def validate_name(name):
        if any(char.isdigit() for char in name):
            return AllErrors().collect_error('name')
        return name

    @staticmethod
    def validate_availability(availability):
        all_hrs = 40
        if int(availability) > all_hrs:
            return AllErrors().collect_error('avail')
        else:
            return availability

    @staticmethod
    def is_exist(list_of_elements, id):
        for element in list_of_elements:
            if element.ID == int(id):
                return AllErrors().collect_error('id')
        return int(id)
