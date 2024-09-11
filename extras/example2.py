import sys

numbers = sys.argv[1:]

print(sum(int(n) for n in numbers))
