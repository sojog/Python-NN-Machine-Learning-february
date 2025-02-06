
## Versiunea 1
file_reader = open("numere.txt", "r")
continut = file_reader.read()
print(continut, type(continut))
file_reader.close()


## Versiunea 2
with open("numere.txt", "r") as file_reader:
    continut = file_reader.read()
    print(continut, type(continut))