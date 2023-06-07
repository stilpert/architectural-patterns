from models import AnimalModel
from controller import Controller
from view import View

if __name__ == "__main__":
    app = View(Controller(AnimalModel()))
    app.run()
