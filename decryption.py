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


def unknown_shift(string): #index of max of list of counters is shift!
    for i in range(26):
        count = 0
        count_lst = []
        maybe_string = known_shift(string, i)
        for x in range(len(maybe_string)):
            count = 0
            if maybe_string[x] in lines:
                count += 1
        count_lst.append(count) #fix this ew but the spirit is there





def get_key(dictionary, value): #lol ew make it better
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