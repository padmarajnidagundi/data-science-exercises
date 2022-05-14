numbers = input().split(" ")

n1, n2, n3 = numbers

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

numbers_list = [n1, n2, n3]

for i in sorted(numbers_list):
    print(i)

print("")

for i in numbers_list:
    print(i)
