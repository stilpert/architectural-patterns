class Person:
    age = None
    name = None

    def __init__(self, name, age=None):
        self.name = name
        self.age = age


class DataLayer:
    # responsible for retrieving data from the db

    persons = []

    def __init__(self):
        # mocks db connection
        self.connect_db()

    def connect_db(self):
        self.persons = [
            Person("Kate", 20),
            Person("Daizy", 17),
            Person("Jack", 15),
            Person("Tom", 30),
        ]

    def get_person_age(self, person_name):
        # returns age of enemy or null
        return next((person.age for person in self.persons if person.name == person_name), None)

    def get_persons_names(self):
        # get all names list
        return [person.name for person in self.persons]





class ApplicationLayer:
    is_init = False
    db = None
    names_cache = None

    def __init__(self, db_layer: DataLayer):
        self.db = db_layer
    
    def load_cache(self):
        if(self.is_init):
            return False
        
        self.names_cache = self.db.get_persons_names()
        self.is_init = True
    
    def cache_init_protection(self):
        if(not self.is_init):
            self.load_cache()

    def get_person_age(self, person_name):
        self.cache_init_protection()
        try:
            if person_name not in self.names_cache: 
                return None
            
            print('self.db.get_person_age(person_name)', self.db.get_person_age(person_name))
            return self.db.get_person_age(person_name)
        except:
            return None

class PresentationLayer:
    application_interface = None
    def __init__(self, application: ApplicationLayer) -> None:
        self.application = application

    def get_person_age(self):
        person_name = input("person name:")
        search_res = self.application.get_person_age(person_name)
        if search_res is None:
            print(f'No [{person_name}] age in db')
        else:
            print(f'[{person_name}] says [{search_res}]')


if __name__ == '__main__':
    db = DataLayer()
    logic = ApplicationLayer(db)
    app = PresentationLayer(logic)

    while True:
        app.get_person_age()