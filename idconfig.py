import json

class idConfig:
    def readFile(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except:
            with open(filename, 'at+') as file:
                data = {}
                data['id'] = []
                json.dump(data, file)
                return data

    @classmethod
    def addId(cls, filename, id):
        data = cls.readFile(filename)
        with open(filename, 'rt+') as file:
            if id not in data['id']:
                data['id'].append(id)
                json.dump(data, file)
                print(f'{id} добавлен в базу данных')
    
    @classmethod
    def removeId(cls, filename, id):
        data = cls.readFile(filename)
        ids = data['id']
        if id in ids:
            del ids[ids.index(id)]
        data['id'] = ids
        with open(filename, 'w') as file:
            json.dump(data, file)
            print(f'{id} удалён из базы данных')