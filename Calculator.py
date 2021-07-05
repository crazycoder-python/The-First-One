# A Nice Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


pup = 'do you want to continue\nYes or No ==>:'

per = 100
print("what do you wanna do?")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Percentage")
running = True
while running:
    choice = input("Enter choice(1/2/3/4/5): ")
    print(
        '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
    if choice in ('1', '2', '3', '4', '5'):
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if choice == '1':
            print(
                '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
            print(num1, "+", num2, "=", add(num1, num2))
            if input(pup) == 'Yes'.casefold():
                continue
            else:
                running = False

        elif choice == '2':
            print(
                '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
            print(num1, "-", num2, "=", subtract(num1, num2))
            if input(pup) == 'Yes'.casefold():
                continue
            elif pup == 'No'.casefold():
                running = False
            else:
                running = False

        elif choice == '3':
            print(
                '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
            print(num1, "*", num2, "=", multiply(num1, num2))
            if input(pup) == 'Yes'.casefold():
                continue
            elif pup == 'No'.casefold():
                running = False
            else:
                running = False


        elif choice == '4':
            print(
                '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
            print(num1, "/", num2, "=", divide(num1, num2))
            if input(pup) == 'Yes'.casefold():
                continue
            elif pup == 'No'.casefold():
                running = False
                print('you dum')
            else:
                running = False
                print('you dum')



        elif choice == '5':
            print(
                '—————————————————————————————————————————————————————————————————————————————————————————————————————————')
            if num1 > num2:
                print('Please Enter A Small Number First!!!')
            else:
                print(num1, "%", num2, "=", num1 * per / num2)
            if input(pup) == 'Yes'.casefold():
                print('ok')
            elif pup == 'No'.casefold():
                running = False
                print('you dum')
            else:
                running = False
                print('you dum')
    elif input(pup) == 'Yes'.casefold():
        continue
    else:
        running = False






