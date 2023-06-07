class Controller:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_animals_names(self):
        return [a.name for a in self.db.animals]

    def add_animal(self, name):
        self.db.add_animal(name)
        return self.get_animals_names()
