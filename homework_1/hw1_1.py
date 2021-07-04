from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
import pickle
import json


class SerializationInterface(ABC):

    @abstractmethod
    def to_json(self, *args, **kwargs):
        pass

    @abstractmethod
    def to_bin(self, *args, **kwargs):
        pass


class ListSerialization(SerializationInterface, List):

    def serialize_json(self, *args, **kwargs):
        serialize_data = json.dumps(self)
        return serialize_data

    def serialize_bin(self, *args, **kwargs):
        serialize_data = pickle.dumps(self)
        return serialize_data


class DictSerialization(SerializationInterface, Dict):

    def serialize_json(self, *args, **kwargs):
        serialize_data = json.dumps(self)
        return serialize_data

    def serialize_bin(self, *args, **kwargs):
        serialize_data = pickle.dumps(self)
        return serialize_data


class TupleSerialization(SerializationInterface, Tuple):
    def serialize_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)


def main():
    serialize_list = ListSerialization()
    serialize_list.append('list item')
    print(serialize_list.serialize_json())

    serialize_dict = DictSerialization()
    serialize_dict['first'] = 'First Data'
    print(serialize_dict.serialize_bin())


if __name__ == '__main__':
    main()