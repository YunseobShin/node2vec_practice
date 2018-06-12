import random

def life_reverse():
    numbers = list(range(1, 46))
    lotto = random.sample(numbers, 6)
    print(lotto)

life_reverse()
