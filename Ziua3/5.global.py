

# varibila globala
variabila = 10
print("variabila=", variabila)


def o_functie():
    # variabila locala
    global variabila
    variabila = 1000
    print("variabila in functie =", variabila)

o_functie()
print("variabila=", variabila)