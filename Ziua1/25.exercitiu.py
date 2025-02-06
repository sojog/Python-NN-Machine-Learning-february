
string = "11,22,33,44,22,33"

numbers = string.split(",")
print(numbers)

unice = []
for i in numbers:
    if numbers.count(i) == 1:
        unice.append(i)
print(unice)