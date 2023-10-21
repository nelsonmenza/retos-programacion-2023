leet_dict = {
    'a': '4',
    'b': '13',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|',
    'm': '|\/|',
    'n': '|\|',
    'o': '0',
    'p': '|2',
    'q': '(_,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': '`/',
    'z': '2'
}

def translate(dict):
    string=input("Enter your string: ")
    new_string=""
    string=string.lower()
    for n in string:
        new_string+=dict[n]
    return new_string

print(translate(leet_dict))