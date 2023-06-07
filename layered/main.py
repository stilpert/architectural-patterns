from layers import ApplicationLayer,DataLayer,PresentationLayer

if __name__ == '__main__':
    db = DataLayer()
    logic = ApplicationLayer(db)
    app = PresentationLayer(logic)

    while True:
        app.get_animal_sound()