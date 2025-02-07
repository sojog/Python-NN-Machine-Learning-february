
# %%
colectie = [100, 200, 300]

def scade_5(x):
    return x - 5

print(list(map(scade_5, colectie)))



# %%
colectie = ["100", "200", "300"]
print(list(map(int, colectie)))


# %%
def putere(x):
    return x ** 2


