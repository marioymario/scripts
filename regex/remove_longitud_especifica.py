import re
def remover_palabras(texto, cantidad_caracteres):

    """Remueve del text los caracterez de longitud especificada"""
    patron = '\\b\\w{%d}\\b'%(cantidad_caracteres)

    regex = re.compile(patron)
    
    return regex.sub('', texto)

cadena = "Python es un lenguage de programacion multiparadigma"
longitud = 2

print(cadena)

print()


resultado  = remover_palabras(cadena, longitud)

print()

print(resultado)