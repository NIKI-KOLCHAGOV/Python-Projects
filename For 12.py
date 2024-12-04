import sys
smallest = sys.maxsize
biggest = -sys.maxsize
n = int(input("Amount of Letters or numbers: "))
for i in range(0, n):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max Number: {biggest}")
print(f"Max Number: {smallest}")
