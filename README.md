Info
====

A stationary source object, suitable for creating sequences of random data with fixed conditional probabilities.

Example Usage
=============

Usage is pretty simple. Just instantiate the source with some data and let it produces sequences for you.

    from nonsense import StationarySource


    def get_lines():
        with open("bruces.txt") as f:
            for line in f:
                yield line.split()


    if __name__ == "__main__":
        lines = list(get_lines())
        g = StationarySource(lines, 1)
        for _ in range(10):
            print " ".join(list(g.generate_sequence()))

And in just 14 lines, we're on our way to starting the next great comedy troupe.

    Hot enough to boil a monkey's bum in here, Bruce.
    Well Bruce, I heard the philosophy department at the University of Walamaloo.
    Blimey, it's hot enough to herself.
    That's a strange expression, Bruce.
    Blimey, it's hot in here, your Majesty," he said and she smiled quietly to introduce man from Pommeyland who is joinin' us this year in here, Bruce.
    Bruce.
    Where's Bruce?
    Blimey, it's hot in the philosophy department at all stuck up.
    Bruce.
    He's not 'ere, Bruce.
