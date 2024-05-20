#!/usr/bin/python3

'''
    Defining a Class BaseModel that has all common attributes/methods
    for other classes
'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Representation of BaseModel Class'''

    def __init__(self, *args, **kwargs):
        '''a function that initialize the BaseModel'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip setting __class__ attribute
                if key in ('created_at', 'updated_at'):
                    # Convert string datetime to datetime object if needed
                    if isinstance(value, str):
                        value = datetime.fromisoformat(value)
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''printing our data'''
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
            Update the public instance attribute updated_at with
            the current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
            returns a dictionary containing all key/value
            of __dict__ of the instance
        '''

        result = self.__dict__.copy()
        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        result['__class__'] = '{}'.format(__class__.__name__)
        return result
