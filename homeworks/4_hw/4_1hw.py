#1. Вычислить число c заданной точностью d
# in Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out 9.000000
# in Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out 8.988
from decimal import Decimal

def accuracy_number(number, accuracy):
    number = Decimal(f"{number}")
    return number.quantize(Decimal(f"{accuracy}"))

print(accuracy_number(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))


