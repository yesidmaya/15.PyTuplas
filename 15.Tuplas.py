#-*- coding: utf-8 -*-

# v = 3.11
# Encontrar el primer caracter que NO se repita en un string

# "abacabad"
# "abacabaabacaba"
# "bcccccccccccyb"


def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

            print(seen_letters[letter])

# "abacabad"
# {
#     'a': (0, 4) # quiere decir que la primera vez que miramos a fue en el indice 0 y la miramos 4 veces
#     'b': (1, 2)
#     'c': (3, 1)
# }

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

# "abacabad"
# [('a', 0), ('d',7)] # lista de tuplas que guarda la letra y el indice donde la vimos por primera vez


# ordernar la lista
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    print('***********')
    print(not_repeated_letters)

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'



if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter NO repetido es: {}'.format(result))