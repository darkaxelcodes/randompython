def findAWord(string1, string2):
    found = False
    if string2.find(string1[0])>0:
        location = string2.index(string1[0])
    if location >= 0:
        for character in string1[1::]:
            if string2.find(character,location)>0:
                location = string2.index(character,location)
                found = True
            else:
                found = False
    return found

print(findAWord('abc', 'bcab'))