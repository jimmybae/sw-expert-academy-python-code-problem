blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {"A": 0, "O": 0, "B": 0, "AB": 0}

for b in blood:
    result[b] += 1

print(result)