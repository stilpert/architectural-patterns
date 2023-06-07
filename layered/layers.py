class Animal:
    sound = None
    name = None

    def __init__(self, name, sound=None):
        self.name = name
        self.sound = sound


class DataLayer:
    # responsible for retrieving data from the db

    animals = []

    def __init__(self):
        # mocks db connection
        self.connect_db()

    def connect_db(self):
        self.animals = [
            Animal("Dog", "Woof"),
            Animal("Cat", "Meow"),
            Animal("Lion", "Roar"),
            Animal("Tiger", "Roar"),
        ]

    def get_animal_sound(self, animal_name):
        # returns sound of enemy or null
        return next((animal.sound for animal in self.animals if animal.name == animal_name), None)

    def get_animals_names(self):
        # get all names list
        return [animal.name for animal in self.animals]





class ApplicationLayer:
    is_init = False
    db = None
    names_cache = None

    def __init__(self, db_layer: DataLayer):
        self.db = db_layer
    
    def load_cache(self):
        if(self.is_init):
            return False
        
        self.names_cache = self.db.get_animals_names()
        self.is_init = True
    
    def cache_init_protection(self):
        if(not self.is_init):
            self.load_cache()

    def get_animal_sound(self, animal_name):
        self.cache_init_protection()
        try:
            if animal_name not in self.names_cache: 
                return None
            
            print('self.db.get_animal_sound(animal_name)', self.db.get_animal_sound(animal_name))
            return self.db.get_animal_sound(animal_name)
        except:
            return None

class PresentationLayer:
    application_interface = None
    def __init__(self, application: ApplicationLayer) -> None:
        self.application = application

    def get_animal_sound(self):
        animal_name = input("Animal name:")
        search_res = self.application.get_animal_sound(animal_name)
        if search_res is None:
            print(f'No [{animal_name}] sound in db')
        else:
            print(f'[{animal_name}] says [{search_res}]')
