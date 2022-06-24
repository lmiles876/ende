import random
import numpy as np
lowers = {x: chr(x) for x in range(97, 123)}




def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


def known_shift(string, shift):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            if int(ord(string[i]))+shift > 122:
                string[i] = lowers[97+(shift - (122 - ord(string[i])))]
            else:
                string[i] = lowers[ord(string[i])+shift]
    string = ''.join(string)
    return string
def unknown_shift(string):
    shift = int(random.uniform(1, 25))
    return known_shift(string, shift), shift
def known_mono(string, cipher):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            string[i] = cipher[ord(str(string[i]))]
    string = ''.join(string)
    return string
def unknown_mono(string):
    cipher = []
    while len(cipher) < 26:
        i = int(random.uniform(0, 26))
        if i not in cipher:
            cipher.append(i)
    cipher = {97 + cipher[i]: chr(97 + i) for i in range(len(cipher))}
    return known_mono(string, cipher), cipher





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
    if np.linalg.det(keymat) == 0:
        raise ValueError('invalid key - key matrix must be invertible')
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


def hill(text, key):
    key = np.matrix(key_setup(key))
    ciphertext = ''
    for i in range(len(text)):
        if i % 3 == 0:
            vectors = []
            for j in range(3):
                if i + j < len(text):
                    vectors.append([get_key(lowers, (text[i + j])) - 97])
                else:
                    vectors.append(0)
            vec = np.matrix(vectors)
            vec = key * vec
            vec = vec % 26
            for i in range(3):
                ciphertext += lowers[vec.item(i) + 97]
    return ciphertext









