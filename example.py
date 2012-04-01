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
