def process_line(line):
    if len(line) % 5 != 0:
        return None, False
    groups = []
    k = len(line) // 5

    for i in range(k):
        g = line[i * 5:(i + 1) * 5]
        if i % 2 == 1:
            g = g[::-1].upper()
        if g not in groups:
            groups.append(g)

    groups.sort()
    return "".join(groups), True
while True:
    s = input()
    if s == "URGENT MATTER":
        break
    res, ok = process_line(s)
    if not ok:
        print("NOT ENOUGH BOOKS")
        break
    print(res)
