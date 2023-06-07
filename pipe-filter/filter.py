import copy

class FilterSuper:
  def __init__(self):
    print("filter")
  
  def filter(self, data):
    return data
  
# sort
class FilterA(FilterSuper):
  def __init__(self):
    FilterSuper.__init__(self)
  
  def filter(self, data):
    data2 = copy.deepcopy(data)
    data2.sort()
    return data2
  
# absolute
class FilterB(FilterSuper):
  def __init__(self):
    FilterSuper.__init__(self)
  
  def filter(self, data):
    return [abs(elem) for elem in data]
  
# normalized
class FilterC(FilterSuper):
  def __init__(self):
    FilterSuper.__init__(self)
  
  def filter(self, data):
    data2 = copy.deepcopy(data)
    f = FilterB()
    data3 = f.filter(data2)
    data3.sort(reverse=True)
    largest = data3[0]
    return [elem / largest for elem in data]