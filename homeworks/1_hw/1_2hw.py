# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
count = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x and not y and not z):
                print(x, y, z)
                count += 1
if count == 2**3:
    print("утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат")
else:
    print(
        "утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для некоторых значений предикат")
