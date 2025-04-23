from datetime import datetime


def dob_calc():
    dob_str = input("Enter your date of birth:")
    dob = datetime.strptime(dob_str, "%d-%m-%Y")
    age = datetime.today().year - dob.year
    if datetime.today().month < dob.month:
        age -= 1
    elif datetime.today().month == dob.month and datetime.today().day < dob.day:
        age -= 1
    return age


print(dob_calc())
