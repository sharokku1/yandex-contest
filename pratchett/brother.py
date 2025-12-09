separator = input()
connector = input()
line = input()
activities = line.split(separator)
bad = [activity for activity in activities
       if "eat" in activity or "sticky" in activity]
print(connector.join(bad))
