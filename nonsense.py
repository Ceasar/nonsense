"""A stationary source.

Produces random sequences of item based on an initial collection of data.
"""
from collections import defaultdict, deque, Counter
import random

__version__ = "0.1.0"

class StationarySource(object):
    """A stationary source object.

    Produces random sequences of item based on an initial collection
    of data.
    """
    def __init__(self, collections, order):
        self._order = order

        self._table = defaultdict(Counter)
        for collection in collections:
            t = self._analyze_collection(collection)
            for key in t:
                self._table[key].update(t[key])

    @property
    def order(self):
        return self._order

    def _source(self):
        """Construct a deque of defaults."""
        return deque([None] * self.order, maxlen=self.order)

    def _analyze_collection(self, collection):
        """Analyze a collection's conditional frequencies."""
        table = defaultdict(Counter)
        q = self._source()
        for item in collection:
            assert item is not None, "Collections cannot contain None's."
            table[tuple(q)][item] += 1
            q.append(item)
        return table

    def _windex(self, lst):
        """Choose a random item from a weighted list of items.

        Accepts a list item and weight pairs."""
        lst = list(lst)
        wtotal = sum(x[1] for x in lst)
        n = random.uniform(0, wtotal)
        for item, weight in lst:
            if n < weight:
                break
            n = n - weight
        return item

    def generate_sequence(self):
        """Generate a stream of random items."""
        key = self._source()
        while True:
            items = self._table[tuple(key)].items()
            if items:
                item = self._windex(items)
                yield item
                key.append(item)
            else:
                break
