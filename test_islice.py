"""
test code for islice
"""

import pytest

from islice import ISlice, SliceIterator


class s_list(list, ISlice):
    pass


class s_tuple(tuple, ISlice):
    pass


class s_string(str, ISlice):
    pass


@pytest.fixture
def simple_list():
    return s_list([2, 4, 3, 5, 6, 7, 3, 8, 2])


@pytest.fixture
def simple_tuple():
    return s_tuple((4, 6, 2, 8, 3, 5, 6))


def test_islice():
    isl = SliceIterator([1, 2, 3])
    assert list(isl[:]) == [1, 2, 3]


def test_non_instantiated():
    """
    if the Iterator is not indexed, it will produce a full slice ([:])
    """
    l = [1, 2, 3, 4, 5]
    si = SliceIterator([1, 2, 3, 4, 5])

    assert list(si) == l


def test_iter_is_itself():

    si = s_list([5, 7, 2]).islice

    assert iter(si) is si
    l = list(si[:2])
    assert iter(si) is si


def test_zero_length():

    si = s_list([]).islice[:]

    assert list(si) == []


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

def test_tuple():
    t = (3, 7, 1, 9, 5, 8, 7, 3, 5, 6)
    st = s_tuple(t)
    assert tuple(st.islice[:2:-1]) == t[:2:-1]


def test_string():
    ss = s_string("this is a string")

    result = "".join(c for c in ss.islice[2::2])
    assert result == "i sasrn"

