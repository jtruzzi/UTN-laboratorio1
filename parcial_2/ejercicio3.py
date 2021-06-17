diccs=[{1:10, 2:20}, {1:30, 4:40}, {4:50, 6:60}]
combined = dict()
for dicc in diccs:
    for key, value in dicc.items():
        if not key in combined or combined[key] < value:
            combined[key] = value    
print(combined)
