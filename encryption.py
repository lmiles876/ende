import random
lowers = {x: chr(x) for x in range(97, 123)}


def known_shift(string, shift):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            if ord(string[i])+shift > 122:
                string[i] = lowers[97+(shift - (122 - ord(string[i])))]
            else:
                string[i] = lowers[ord(string[i])+shift]
    string = ''.join(string)
    return string


def unknown_shift(string):
    shift = int(random.uniform(1, 25))
    print('shift used: ', shift)
    return known_shift(string, shift)

    # for i in range(len(string)):
    #     if 97 <= ord(string[i]) <= 122:
    #         if ord(string[i])+shift > 122:
    #             string[i] = lowers[97+(shift - (122 - ord(string[i])))]
    #         else:
    #             string[i] = lowers[ord(string[i])+shift]
    # string = ''.join(string)
    # print('shift used: ', shift)
    # return string


def known_mono(string, cipher):
    string = list(string.lower())
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            string[i] = cipher[ord(string[i])]
    string = ''.join(string)
    return string


def unknown_mono(string):
    cipher = []
    while len(cipher) < 26:
        i = int(random.uniform(0, 26))
        if i not in cipher:
            cipher.append(i)
    cipher = {97 + cipher[i]: chr(97 + i) for i in range(len(cipher))}
    print('cipher used:', cipher)
    return known_mono(string, cipher)



