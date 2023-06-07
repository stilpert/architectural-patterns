import pytest
from filter import FilterA, FilterB, FilterC

@pytest.fixture
def sample_data():
    return [3, -2, 1, -5, 4]

def test_filterA(sample_data):
    filter_a = FilterA()
    filtered_data = filter_a.filter(sample_data)
    assert filtered_data == [-5, -2, 1, 3, 4]

def test_filterB(sample_data):
    filter_b = FilterB()
    filtered_data = filter_b.filter(sample_data)
    assert filtered_data == [3, 2, 1, 5, 4]

def test_filterC(sample_data):
    filter_c = FilterC()
    filtered_data = filter_c.filter(sample_data)
    assert filtered_data == [0.6, -0.4, 0.2, -1.0, 0.8]