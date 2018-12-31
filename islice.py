#!/usr/bin/env python3

"""
islice mixin -- makes an easy to access slice-style iterator

"""


class slice_list(list):

    @property
    def islice(self):
        return ISlice(self)


class islice_mixin:
    @property
    def islice(self):
        return ISlice(self)


class ISlice:
    """
    mixin that adds an iterable acces with slice semantics
    """

    def __init__(self, seq):
        self.seq = seq

    def __iter__(self):
        self.current = self.start - self.stride
        return self

    def __next__(self):
        print("in next")
        self.current += self.stride
        if  ((self.stride > 0 and self.current >= self.stop) or
             (self.stride < 0 and self.current <= self.stop)):
            raise StopIteration
        return self.seq[self.current]

    def __getitem__(self, slc):
        print("in index")
        print(slc)
        if not isinstance(slc, slice):
            raise TypeError(".islice only works with single slices")
        self.start, self.stop, self.stride = slc.indices(len(self.seq))
        print(self.start, self.stop, self.stride)
        return self
