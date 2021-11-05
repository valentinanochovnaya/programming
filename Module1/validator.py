import re
import os
import sys
import datetime as dt
from custom_exeptions import *


class Validator:
    def __init__(self):
        pass

    @classmethod
    def choose_validate_function(cls, key_, value_):
        validate_dict = {
            'ID': cls.validate_number,
            'username': cls.validate_name,
            'budget': cls.validate_budget,
            'start_date': cls.validate_date,
            'end_date': cls.validate_date,
            'city': cls.validate_city
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
    def validate_budget(value):
        return float(value)

    @staticmethod
    def validate_city(city):
        city_list = ['Rome', 'Paris', 'Naples', 'Vienna']
        if city in city_list:
            return city
        else:
            return AllErrors().collect_error('city')

    @staticmethod
    def validate_name(name):
        if any(char.isdigit() for char in name):
            return AllErrors().collect_error('name')
        return name

    @staticmethod
    def is_exist(list_of_elements, id):
        for element in list_of_elements:
            if element.ID == int(id):
                return AllErrors().collect_error('id')
        return int(id)

    @staticmethod
    def validate_date(date):
        if isinstance(date, str):
            try:
                return dt.datetime.strptime(date, '%Y-%m-%d')
            except:
                print(f'Wrong data!')
            sys.exit()
        return dt.datetime.strptime(date, '%Y-%m-%d')

    @staticmethod
    def is_name_exists(name, list_of_elements):
        for element in list_of_elements:
            if element.username == name:
                raise AllErrors().collect_error('name_exists')
        return name

