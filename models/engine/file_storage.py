#!/usr/bin/python3

'''
Defining a class FileStorage
'''

import json


class FileStorage():
    '''Representation of FileStorage'''
    __file_path = "file.json"
    __objects = {}

    @property
    def(self):
        '''Return the dictionary objecrts'''
        return self.__objects

    @new.setter
    def new(self, obj):
        '''Setter function'''
        __objects[id] = obj

    def save(self):
        '''Serializes __object to json file'''
        with open("file.json", mode="w", encoding="utf-8") as f:
            json.dumps(self.__objects, f)

    def reload(self):
        '''deserializes json file to the object'''
        with open("file.json", mode"r", encoding="utf-8") as f:
            result = json.load(f)

            return result
