import numpy as np
import sympy
import encryption as e
lowers = {x: chr(x) for x in range(97, 123)}

with open('dict_official.txt', 'r') as f1:
    lines = f1.readlines()
    lines = lines[0].split(' ')


def known_shift(string, shift):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            if ord(string[i])-shift < 97:
                string[i] = lowers[122 - (shift - (ord(string[i])-97))]
            else:
                string[i] = lowers[ord(string[i])-shift]
    string = ''.join(string)
    return string


def unknown_shift(string):
    most = 0
    shift = 0
    for i in range(1, 26):
        count = 0
        maybe_string = known_shift(string, i).split()
        for x in range(len(maybe_string)):
            if maybe_string[x] in lines:
                count += 1
        if count > most:
            most = count
            shift = i
    return known_shift(string, shift), shift


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


def known_mono(string, cipher):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            string[i] = chr(get_key(cipher, string[i]))
    string = ''.join(string)
    return string


def key_setup(key):
    if len(key) != 9:
        raise ValueError('please enter a 9 letter key')
    key = key.lower()
    keymat = []
    for i in range(0, int(len(key)), int(len(key)/3)):
        keymat.append(list(key[0+i:i+int(len(key)/3)]))
    for i in range(len(keymat)):
        for j in range(int(len(key)/3)):
            keymat[i][j] = int(get_key(lowers, keymat[i][j]) - 97)
    return keymat


def string_setup(string):
    string = (string.replace(' ', '')).lower()
    count = 0
    while len(string) % 3 != 0:
        string += 'a'
        count += 1
    stringmat = []
    for i in range(0, int(len(string)), 3):
        stringmat.append(list(string[0+i:i+3]))
    for i in range(len(stringmat)):
        for j in range(3):
            stringmat[i][j] = int(get_key(lowers, stringmat[i][j]) - 97)
    return stringmat, count


def bezout(x):
    for y in range(0, 26):
        if (x*y) % 26 == 1:
            return y
    return 0


def hill(text, key):
    key = key_setup(key)
    text = text.lower()
    key_sympy = sympy.Matrix(key)
    adjoint_matrix = key_sympy.adjugate() % 26
    key = np.matrix(key)
    det = round(np.linalg.det(key)) % 26
    multiplicative_inverse = bezout(det)
    inverse = (multiplicative_inverse * adjoint_matrix) % 26
    plaintext = ''
    alphabet = [chr(x) for x in range(97, 123)]

    for i in range(len(text)):
        if i % 3 == 0:
            vectors = []
            for j in range(3):
                if i + j < len(text):
                    vectors.append([alphabet.index(text[i + j])])
                else:
                    vectors.append(0)
            vec = np.matrix(vectors)
            vec = inverse * vec
            vec = vec % 26
            for i in range(3):
                plaintext += lowers[vec[i] + 97]
    return plaintext



