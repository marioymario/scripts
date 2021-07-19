from functools import reduce

lista = [2, 3, 4, 5, 6]
lista2 = [1, 4, 5, 4, 7]

e = reduce(lambda x, y : x + y, lista)
print(e) # wont print because is a function
