# Will Hearn
# SEC 207.91-21
# 9/14/21
import random


# Does a list of things
def do_things():
    print(input("What is your name? "))

    num = int(input("Enter a number: "))
    print(num * num)

    count = 0
    for x in input("Enter a word: "):
        if x == " ":
            pass
        else:
            count += 1
    print(count)

    print("Your random number is:", random.randint(1, 10))


# Main Method
if __name__ == '__main__':
    do_things()
