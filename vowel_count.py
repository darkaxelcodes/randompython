def vowel_count(sentence):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

sentence = input("Enter the sentence: ")
count = vowel_count(sentence)
print("The total number of vowels in the entered sentence are {}".format(count))