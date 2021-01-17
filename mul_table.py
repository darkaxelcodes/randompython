def mul_table(number):
    i = 1
    while i <= 10:
        print("{} x {} = {}".format(number, i, number*i))
        i += 1

number = int(input("Enter the number: "))
mul_table(number)