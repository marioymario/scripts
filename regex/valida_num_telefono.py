import re

"""saca numero de telefono que empiesa con 7, 8 o 9
y de diez digitos
imprime si si el numero es valido y no si no, sin comillas"""

# usuario ingrsa los numeros
"""
asi,
import valida_num_telefono
2
9874561232
4567894562
"""

phone_numbers = [input() for _ in range(int(input()))
                 ]  # this will store the numbers

pattern = '^[789]\d{9}$'
validator = re.compile(pattern)

for p in phone_numbers:
    print('YES' if validator.search(p) else 'NO')
