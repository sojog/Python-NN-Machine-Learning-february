
import random

def functia_a() -> None:
    pass

def functia_b() -> int:
    return random.randint(1, 20)


# type hints
def functia_c(param1:int, param2:int) -> float:
    return param1 / param2

print(functia_a())
functia_b()
print(functia_c(100, 2))
print(functia_c(100.03, 2))