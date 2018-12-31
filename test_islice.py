"""
test code for islice
"""

import pytest

from islice import ISlice, slice_list, islice_mixin


@pytest.fixture
def simple_list():
    return slice_list([2, 4, 3, 5, 6, 7, 3, 8, 2])


@pytest.fixture
def tuple_mixedin():
    class slice_tuple(tuple, islice_mixin):
        pass
    return slice_tuple((4, 6, 2, 8, 3, 5, 6))


def test_islice():
    isl = ISlice([1, 2, 3])
    slicer = isl[:]
    print(slicer)


def test_slice_list1(simple_list):
    l2 = []
    for i in simple_list.islice[:]:
        print(i)
        l2.append(i)
    assert l2 == simple_list


def test_slice_simple_index(simple_list):
    with pytest.raises(TypeError):
        simple_list.islice[4]


def test_slice_stride(simple_list):
    result = list(simple_list.islice[::2])
    assert result == simple_list[::2]


def test_slice_negative(simple_list):
    result = list(simple_list.islice[::2])
    assert result == simple_list[::2]


def test_slice_reverse(simple_list):
    result = list(simple_list.islice[::-1])
    assert result == simple_list[::-1]


def test_mixedin(tuple_mixedin):
    result = tuple(tuple_mixedin[:2:-1])
    assert result == tuple_mixedin[:2:-1]

