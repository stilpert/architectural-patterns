class Controller:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_notifications_texts(self):
        return [a.text for a in self.db.notifications]

    def add_notification(self, text):
        self.db.add_notification(text)
        return self.get_notifications_texts()
