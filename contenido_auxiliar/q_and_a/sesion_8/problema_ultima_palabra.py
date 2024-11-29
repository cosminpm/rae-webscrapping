# Given a string s consisting of words and spaces, return the length of the last word in the string.

# Casos de Prueba
# Ramon
# Juan Ramon
#
# Juan Ramon Perez del Castillo


def length_last_word(word: str) -> int:
    contador = 0
    for i in range((len(word) - 1), -1, -1):
        letra = word[i]
        if letra == " ":
            break
        contador += 1
    return contador


if __name__ == '__main__':
    case = "abc patata"
    res = length_last_word(case)
    ...