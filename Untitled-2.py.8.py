A = {'a': 100, 'b': 200, 'c': 300}
B = {'a': 300, 'b': 200, 'd': 400}
result = {}
for key in set(A.keys()) | set(B.keys()):
    result[key] = A.get(key,0) + B.get(key,0)
print("result" , result)