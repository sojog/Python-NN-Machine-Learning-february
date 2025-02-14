import time

timpul_actual = time.time()
print(timpul_actual)

time.sleep(4)

noul_timp = time.time()
print(noul_timp)

delta = noul_timp - timpul_actual
print(delta)