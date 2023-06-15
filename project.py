def user_details():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    marital_status = input("Are you married? (yes/no) ")
    money = input("Do you have money? ")

    if money.lower() == "yes":
        print("Good job, You can live in this cruel world :),", first_name + "!")
    else:
        print("Sorry you don't have the right to live in this world Mr,", first_name + "!")

user_details()
