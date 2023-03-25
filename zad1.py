numbers = input("Podaj liczby po przecinku")

numbers_list = numbers.split(",")
maximum = float(numbers_list[0])
minimum = float(numbers_list[0])

for x in numbers_list:
    x = float(x)
    if x > maximum:
        maximum = x
    elif x < minimum:
        minimum = x

print("Maksimum: ", maximum, '\n')
print("Minimum: ", minimum, '\n')
