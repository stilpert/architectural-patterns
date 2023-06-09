import copy


class Filter:
    def __init__(self):
        print("filter")

    def filter(self, data):
        return data


class PositiveFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def filter(self, data):
        data2 = copy.deepcopy(data)
        filter(lambda score: score >= 0, data2)
        return data2


class NegativeFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def filter(self, data):
        data2 = copy.deepcopy(data)
        filter(lambda score: score < 0, data2)
        return data2


class AbsFilter(Filter):
    def __init__(self):
        Filter.__init__(self)

    def filter(self, data):
        return [abs(elem) for elem in data]

