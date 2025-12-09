n = int(input())
previous = list(map(int, input().split()))

for i in range(n - 1):
    current = list(map(int, input().split()))
    used = set()
    result = []
    for x in current:
        if x % 4 == 0 and x not in previous and x not in used:
            used.add(x)
            result.append(x)
    print(" * ".join(map(str, result)))
    previous = current
