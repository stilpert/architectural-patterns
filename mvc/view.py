import os
from models import NotificationModel
from controller import Controller


class View:
    def __init__(self, controller):
        self.controller = controller

    def clear_screen(self):
        os.system('cls')

    def print_delimeter(self):
        print('_______________________')

    def print_notification(self):
        texts = self.controller.get_notifications_texts()
        self.clear_screen()

        self.print_delimeter()

        if not len(texts):
            print('No notifications')

        for i in range(len(texts)):
            print(f'{i+1}. {texts[i]}')

        self.print_delimeter()

    def run(self):
        while True:
            self.print_notification()
            new_notification = input('\nEnter new notification-->\n')
            if (new_notification):
                self.controller.add_notification(new_notification)


if __name__ == "__main__":
    app = View(Controller(NotificationModel()))
    app.run()
