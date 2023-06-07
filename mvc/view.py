import os


class View:
    def __init__(self, controller):
        self.controller = controller

    def clear_screen(self):
        os.system('cls')

    def print_delim(self):
        print('===============')

    def print_animals(self):
        names = self.controller.get_animals_names()
        self.clear_screen()

        self.print_delim()

        if not len(names):
            print('No animals')

        for i in range(len(names)):
            print(f'{i+1}. {names[i]}')

        self.print_delim()

    def run(self):
        while True:
            self.print_animals()
            new_animal = input('\nEnter new animal-->\n')
            if (new_animal):
                self.controller.add_animal(new_animal)
