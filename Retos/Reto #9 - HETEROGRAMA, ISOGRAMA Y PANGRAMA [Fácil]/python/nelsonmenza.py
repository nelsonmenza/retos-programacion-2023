def heterograma(string):
    newString = [chr for chr in string]
    for chr in newString:
        n = 0
        for i in string:
            if i.lower() == chr.lower():
                n += 1
        if n > 1:
            return False
    return True


def isograma(string):
    newString = [chr for chr in string]
    for chr in newString:
        n = 0
        for i in string:
            if i.lower() == chr.lower():
                n += 1
        if n == 2:
            return True
    return False


def pangrama(string):
    

print(name.isalpha())
