number = int(input("Enter the number to check prime or not : "))

flag = False

if number == 0 or number == 1:

    print("Not a prime number")

elif number > 1:

    for i in range (2, number):

        if number % i == 0:

            flag=True

            break

    if flag == True:

        print("Not a prime number")

    else:

        print("Prime number")