def word_count(sentence):
    count = 0
    for word in sentence:
        if word ==' ':
            count += 1
    count += 1
    return count

sentence = input("Enter the sentence: ")
count = word_count(sentence)
print("The total number of words in the entered sentence are {}".format(count))
