import sys
from random import randint


def generate_numbers(n):
    return [randint(1, 1000) for x in range(n)]


def main():
    if len(sys.argv[1:]) >= 2:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        f = open(filename, "w")
        contents = [str(x) for x in generate_numbers(n)]
        f.write(" ".join(contents))
        f.write("\n")
        f.close()

if __name__ == "__main__":
    main()
