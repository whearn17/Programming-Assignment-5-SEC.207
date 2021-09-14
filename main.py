# Will Hearn
# SEC 207.91-21
# 9/14/21

# Printing Method
def print_name():
    print(input("What is your name? "))


def multiply_number():
    num = int(input("Enter a number: "))
    print(num * num)


def count_letters():
    count = 0
    for x in input("Enter a word: "):
        if x == " ":
            pass
        else:
            count += 1
    print(count)


# Main Method
if __name__ == '__main__':
    print_name()
    multiply_number()
    count_letters()
