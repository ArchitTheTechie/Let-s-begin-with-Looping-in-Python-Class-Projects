#Creating a python Program which checks the eligibility for a medical exam

medicalCert = input("Do you have a medical certicificate? (Y/N)")

if medicalCert == 'N':
    print("You are not eligible for the exam")
else:
    print("You are eligible for the exam")

    attendence = int(input("Enter your attendence marks : "))

    if attendence >= 50 :
        print("You are allowed for the exam")
    else:
        print("You are not allowed for the exam")   