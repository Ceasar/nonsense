from collections import defaultdict, deque, Counter
import os
import random
import string


def get_words(dir_='words'):
    """Get all English words.
    
    Each file should contain exactly one word per line.
    """
    for dirpath, _, filenames in os.walk(dir_):
        for filename in filenames:
            with open(os.path.join(dirpath, filename)) as f:
                for line in f:
                    yield line


def empty(order):
    """Build a deque of empty strings."""
    return deque([" "] * order, maxlen=order)


def analyze_word(word, order):
    """Analyze a word's frequencies."""
    table = defaultdict(Counter)
    q = empty(order)
    for letter in word:
        table[tuple(q)][letter] += 1
        q.append(letter)
    return table


def generate_table(words, order):
    """Generate a frequency table of order-n for the given words."""
    table = defaultdict(Counter)
    for word in words:
        t = analyze_word(word, order)
        for prefix in t:
            table[prefix].update(t[prefix])
    return table


def windex(lst):
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


def generate_word(t, order):
    """Generate a random word using a given table."""
    letters = []
    key = empty(order)
    while "\n" not in key:
        letter = windex(t[tuple(key)].items())
        letters.append(letter)
        key.append(letter)
    return "".join(letters[:-1])


if __name__ == "__main__":
    import sys
    order = int(sys.argv[1])
    t = generate_table(get_words(), order)
    for _ in range(100):
        print generate_word(t, order)
