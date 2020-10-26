import util
import datetime

lastNum = [0, 1]
length = 0
numbers_ = []


class numbers:


    def getLength(self):
        # try:
        length = int(input("Length: "))
        # print(type(length))
        # print(length)
        print(lastNum[0])
        print(lastNum[1])
        for i in range(length):
            self.nextNumber()

    # except Exception as e:
    #     util.handleError(e, datetime.datetime.now())

    @staticmethod
    def nextNumber():
        # try:
        nextNumber = lastNum[0] + lastNum[1]
        lastNum[0] = lastNum[1]
        lastNum[1] = nextNumber
        if lastNum[1] == nextNumber:
            print(lastNum[1])
        else:
            util.handleError("My Own Error", 10)
        # except Exception as e:
        #     util.handleError(e, datetime.datetime.now())


class is_a_number:

    def __init__(self):
        numbers_.append(lastNum[0])
        numbers_.append(lastNum[1])
        for i in range(9999):
            nextNumber = lastNum[0] + lastNum[1]
            lastNum[0] = lastNum[1]
            lastNum[1] = nextNumber
            if lastNum[1] == nextNumber:
                numbers_.append(lastNum[1])
        self.check()

    def check(self):
        # print(numbers_)
        num = int(input("Number: "))
        if num in numbers_:
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is not a Fibonacci number.")

    @staticmethod
    def nextNumber():
        # try:
        nextNumber = lastNum[0] + lastNum[1]
        lastNum[0] = lastNum[1]
        lastNum[1] = nextNumber
        if lastNum[1] == nextNumber:
            numbers_.append(lastNum[1])
        else:
            util.handleError("My Own Error", 10)
        # except Exception as e:
        #     util.handleError(e, datetime.datetime.now())

while True:
    choice = input("What do you want to do? A for get fibonacci number or B for Fibonacci checker: ").lower()
    if choice == 'a':
        numbers().getLength()
    elif choice == 'b':
        is_a_number()
