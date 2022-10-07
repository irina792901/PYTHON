# 1. Вычислить число c заданной точностью d

from decimal import Decimal


def accuracy(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))


# --------------------------------------- 2 вариант

num = float(input('Enter a real number: '))

_, accu = input("Enter the required accuracy '0.0001': ").split(".")
print(f"{num:.{len(accu)}f}")
