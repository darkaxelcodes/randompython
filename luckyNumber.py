def sumOfDigits(numberList):
    sum = 0
    for digit in numberList:
        sum += int(digit)
    numberList = list(str(sum))
    return numberList
    
def luckyNumber(birthday):
    luckyNumberList = list(str(birthday))
    luckyNumberList = sumOfDigits(luckyNumberList)
    while len(luckyNumberList)>1:
        luckyNumberList = sumOfDigits(luckyNumberList)
    return int(luckyNumberList[0])

try:
    birthday = int(input("Enter your birthday: "))
    lNumber = luckyNumber(birthday)
    print("Your lucky number is : {}".format(lNumber))
except ValueError:
    print("Enter a numeric data!")