string = "Banana"

char = input("Enter any one character from the word Banana : ")

i = 0

count = 0

while i < len(string):


    if string[i] == char:

        count = count + 1

    i = i + 1

print("Number of character occurence for ", char, "is ", count)