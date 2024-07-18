import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float * 5 

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


import random 

game = random.randint(0, 1)
if game == 1:
  print("Tails")
else:
    print("Heads")
