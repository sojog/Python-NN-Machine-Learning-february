

print("Hello")

# print("9" * 2.0)

while True:
    nr = input("Introduceti un numar\n")
    try:
        nr = int(nr)
        print("Ati introdus:", nr)
    except:
        print("Ceea ce ai introdus nu este un numar")
    finally:
        print("Linie care se executa oricum")