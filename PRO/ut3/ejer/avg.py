import sys

values = sys.argv[1:]
values = [int(values[i]) for i in range(len(values))]
avg = sum(values) / len(values)
print(avg)
