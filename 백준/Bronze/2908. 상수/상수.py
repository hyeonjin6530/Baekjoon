a, b = input().split()
a = int("".join(reversed(a)))
b = int("".join(reversed(b)))

print(max(a, b))