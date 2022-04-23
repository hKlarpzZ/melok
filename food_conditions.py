import json

class FoodStorage:
    def readFile():
        filename = 'food_storage.json'
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return data
        except:
            with open(filename, 'at+') as file:
                data = {}
                data['counter'] = 0
                data['lots'] = []
                json.dump(data, file)
                return data

    @classmethod
    def addFood(cls, Food_obj):
        filename = 'food_storage.json'
        data = cls.readFile()
        with open(filename, 'rt+') as file:
            data['counter'] += 1
            id = data['counter']
            to_json_food_obj = []
            to_json_food_obj.append(id)
            to_json_food_obj.append(Food_obj.get_name())
            to_json_food_obj.append(Food_obj.get_ingredients())
            to_json_food_obj.append(Food_obj.get_preparation())
            to_json_food_obj.append(Food_obj.get_portions())
            to_json_food_obj.append(Food_obj.get_img())
            to_json_food_obj.append(Food_obj.get_type())
            data['lots'].append(to_json_food_obj)
            json.dump(data, file)
            # if id not in data['id']:
            #     data['id'].append(id)
            #     json.dump(data, file)
            #     print(f'{id} добавлен в базу данных')
    
    # @classmethod
    # def removeId(cls, filename, id):
    #     data = cls.readFile(filename)
    #     ids = data['id']
    #     if id in ids:
    #         del ids[ids.index(id)]
    #     data['id'] = ids
    #     with open(filename, 'w') as file:
    #         json.dump(data, file)
    #         print(f'{id} удалён из базы данных')


class Food_obj:
    # Изначальные значения(Дефолтные)
    name = 'noname'
    ingredients = []
    preparation = []
    portions = 1
    img = ''

    # Создание(объявление) объекта класса
    def __init__(self, name=name, ingredients=ingredients, preparation=preparation, portions=portions, img=img) -> None:
        if name == 'noname':
            print('name is empty')
            # raise KeyError
        self.name = name
        if ingredients == []:
            print('ingredients are empty')
            # raise KeyError
        self.ingredients = ingredients
        if preparation == []:
            print('preparation is empty')
            # raise KeyError
        self.preparation = preparation
        self.portions = portions
        self.img = img

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients

    def get_preparation(self):
        return self.preparation

    def get_portions(self):
        return self.portions

    def get_img(self):
        return self.img