vocales = ["a","e","i","o","u"]
print(vocales)
print(vocales[0],vocales[1],sep="*")
print(f"Vocales: {0}")

for i in range(1):
    print(i,end="-")

for i in range(len(vocales)):
    print(f"{vocales[i]}", end=",")
else:
    print()

print(f"Logitud de vocales: {len(vocales)}")

for c in vocales:
    print(f"Vocales: {c}")
    
for c in vocales:
    if c== "b":
        break
else:
    print("No se ha encontrado el carácter b")