lista = [2, 3, 4, 5, 6]
lista2 = [1, 4, 5, 4, 7]
# take function as a first arg and
# returns a boolean

## this filters the even values
##
c = filter(lambda x : x%2==0, lista )
print(c) # wont print because is a function
print(list(c))
## now all the values greater than 5
d = filter(lambda x : True if x >= 5 else False, lista)
print(d) # wont print because is a function
print(list(d))