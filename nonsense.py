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

    collections must not contain any None's. They are reserved for interal
    signaling.
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

    def _weighted_choice(self, item_weights):
        """Choose a random item from a weighted list of items.

        Raises a ValueError if no items are provided."""
        item, weight = (None, 0)
        for item2, weight2 in item_weights:
            n = random.randint(1, weight + weight2)
            if n <= weight2:
                item, weight = item2, weight + weight2
        if item is None and weight == 0:
            raise ValueError("No items supplied.")
        else:
            return item

    def generate_sequence(self):
        """Generate a stream of random items."""
        key = self._source()
        while True:
            items = self._table[tuple(key)].iteritems()
            try:
                item = self._weighted_choice(items)
            except ValueError:
                break
            else:
                yield item
                key.append(item)
