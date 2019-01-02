#!/usr/bin/env python3

"""
islice mixin -- makes an easy to access slice-style iterator
"""

class ISlice:
    """
    mixin that adds an iterator with slice semantics
    """
    @property
    def islice(self):
        return SliceIterator(self)


class SliceIterator:
    def __init__(self, seq):
        self.seq = seq
        self.start = 0
        self.stop = len(seq)
        self.stride = 1
        self.current = -1

    def __iter__(self):
        return self

    # def __repr__(self):
    #     return f"SliceIterator({self.seq!r})"

    def __str__(self):
        return f"SliceIterator({self.seq!s})"

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
        self.current = self.start - self.stride
        return self

