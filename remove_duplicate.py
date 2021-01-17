def remove_duplicate(sentence):
    distinct = []
    for letter in sentence:
        if letter == ' ':
            distinct.append(letter)
        if letter not in distinct:
            distinct.append(letter)
    return distinct

sentence = input("Enter the sentence: ")
distinct = remove_duplicate(sentence)
for i in range(len(distinct)):
    print(distinct[i],end='')