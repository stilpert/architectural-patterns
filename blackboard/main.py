from pprint import pprint
from blackboard import Blackboard, Controller, Sedan, Suv, Truck

if __name__ == '__main__':
    blackboard = Blackboard()

    blackboard.add_car(Truck(blackboard))
    blackboard.add_car(Suv(blackboard))
    blackboard.add_car(Sedan(blackboard))

    res = Controller(blackboard).run()

    pprint(res)
