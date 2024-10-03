for i in range (10):
    if i == 5:
        break

    print (i)

for i in range (10):
    if i % 2 == 0:
        continue

    print (i)


total = 0
while total < 100:
    number = int (input("Ingrese un número: "))
    total += number

print (f"Total acumulado: {total}")