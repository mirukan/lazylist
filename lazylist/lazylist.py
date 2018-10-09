import collections.abc
from itertools import chain, islice


class LazyList(collections.abc.MutableSequence):
    def __init__(self, iterable):
        self._nonlazy = []
        self._lazy    = iter(iterable)

        self.is_fully_loaded = False


    def __len__(self):
        self._delazify()
        return len(self._nonlazy)


    def _delazify(self, index=None):
        if index is None:
            self._nonlazy.extend(self._lazy)
            self.is_fully_loaded = True
            return

        if isinstance(index, slice):
            if (index.start or 0) < 0 or (index.stop or -1) < 0:
                self._delazify()
                return

            index = range(index.start or 0, index.stop, index.step or 1)[-1]

        if index < 0:
            self._delazify()
            return

        islice_start = index - len(self._nonlazy) + 1

        if islice_start < 0:
            # elements are already unlazyfied
            return

        self._nonlazy.extend(
            islice(self._lazy, islice_start)
        )


    def __getitem__(self, index):
        self._delazify(index)
        return self._nonlazy[index]


    def __delitem__(self, index):
        self._delazify(index)
        del self._nonlazy[index]


    def __setitem__(self, index, value):
        self._delazify(index)
        self._nonlazy[index] = value


    def insert(self, index, value):
        if index:
            self._delazify(index-1)
        self._nonlazy.insert(index, value)


    def __iter__(self):
        yield from self._nonlazy

        for value in self._lazy:
            self._nonlazy.append(value)
            yield value


    def append(self, value):
        self._lazy = chain(self._lazy, (value,))


    def extend(self, values):
        self._lazy = chain(self._lazy, values)


    def clear(self):
        self._nonlazy, self._lazy = [], iter(())


    def __str__(self):
        reprs = list(map(repr, self._nonlazy))

        if not self.is_fully_loaded:
            reprs.append("...")

        return "[%s]" % ", ".join(reprs)


    def __repr__(self):
        return f"LazyList({self})"
