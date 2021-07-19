lista = [2, 3, 4, 5, 6]
lista2 = [1, 4, 5, 4, 7]
"""map is a function that pass two args"""
a = map(lambda x : x * 2, lista)
print(a) # wont print because is a function
print(list(a))
b = map(lambda x, y : x +y, lista, lista2)
print(b) # wont print because is a function
print(list(b))