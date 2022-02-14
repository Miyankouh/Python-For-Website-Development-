import json
from abc import ABC, abstractmethod


class StorageAbstract(ABC):

    @abstractmethod
    def store(self, data, *args):
        pass


class MongoStorage(StorageAbstract):

    def store(self, data, *args):
        raise NotImplementedError()


class FileStorage(StorageAbstract):

    def store(self, data, filename, *args):
        with open(f'fixtures/adv/{filename}.json', 'w') as f:
            f.write(json.dumps(data))
        print(f'fixtures/adv/{filename}.json')
