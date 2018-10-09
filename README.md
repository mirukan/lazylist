lazylist
========

Lazy lists for Python.

```python3
>>> from lazylist import LazyList
>>> l = LazyList(range(10))                                                                                        
>>> l
LazyList([...])

>>> l[3]
3
>>> l
LazyList([0, 1, 2, 3, ...])

>>> l[-1]
9
>>> l
LazyList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
