
class Factory:
    __instance = None
    item_list = []
    item_key = 0

    @staticmethod
    def get_instance():
        if Factory.__instance == None:
            Factory()
        return Factory.__instance

    def __init__(self):
        if Factory.__instance != None:
            raise Exception('\n\t This class is Singleton \n')
        else:
            Factory.__instance = self

    def add_item(self, class_object, description):
        item = Item(class_object, description)
        self.item_list.append(item)
        self.item_key += 1
    
    def get_specific_item(self, desc):
        for item in self.item_list:
            if item.get_description() == desc:
                return item
        return None
    
    def get_item_list(self):
        return self.item_list


class Item:
    class_object = None
    description = ''

    def __init__(self, class_object, description):
        self.class_object = class_object
        self.description = description
    
    def get_object(self):
        return self.class_object
    
    def get_description(self):
        return self.description
