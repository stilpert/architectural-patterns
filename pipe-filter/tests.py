import pytest
from filter import PositiveFilter, AbsFilter, NegativeFilter


@pytest.fixture
def sample_data():
    return [3, -2, 1, -5, 4]


def test_PositiveFilter(sample_data):
    filter_a = PositiveFilter()
    filtered_data = filter_a.filter(sample_data)
    assert filtered_data == [3, 1, 4]


def test_AbsFilter(sample_data):
    filter_b = AbsFilter()
    filtered_data = filter_b.filter(sample_data)
    assert filtered_data == [3, 2, 1, 5, 4]


def test_NegativeFilter(sample_data):
    filter_c = NegativeFilter()
    filtered_data = filter_c.filter(sample_data)
    assert filtered_data == [-2, -5]
