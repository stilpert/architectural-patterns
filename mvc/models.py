class Notification:
    def __init__(self, text) -> None:
        self.text = text


class NotificationModel:
    def __init__(self) -> None:
        self.notifications = []

    def add_notification(self, text):
        self.notifications.append(Notification(text))
