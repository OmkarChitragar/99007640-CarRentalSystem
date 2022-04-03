import bcrypt


def dashboard():
    file = open("rental.txt", "r")
    append = open("rental.txt", "a")
    choice = input("| Press 0 to rent a car |")
    if choice == "0":
        car_list = []
        price_list = []
        details = []
        for lines in file:
            lines = lines.rstrip()
            temp_list = lines.split()
            car_list.append(temp_list[0])
            price_list.append(temp_list[1])
            temp_details = ""
            for texts in range(2, len(temp_list)):
                temp_details += "" + temp_list[texts]
            details.append(temp_details)
            car = input("Car name that you want to rent: ")

            if car not in car_list:
                print("Sorry! Not available right now.")
            else:
                day = input("No. of days you want to rent: ")
                index = car_list.index(car)
                temp_price = price_list[index]
                price = ""

                for num in range(len(temp_price) - 3):
                    price = price + temp_price[num]
                total_amount = int(price) * int(day)
                print("\n" * 2)
                print(">Price to pay: ")
                print("Rs." + str(total_amount))
                print(">Car details:")
                print(details[index])
                print("\n" * 2)
                confirm = input("| Press 0 to proceed for payment |")

                if confirm == "0":
                    print(" Your total amount is Rs." + str(total_amount))
                    payment = input("\n| Press 1 to confirm payment |")

                    if payment == "1":
                        print("Payment successful!\n")
                        print("Your booking has been confirmed.\n")
                        print("Booking details: ")
                        print(">Car booked     :", car)
                        print(">Time period    :", day, "days")
                        print(">Car details    :", details[index])
                        print(">Payment details: Rs." + str(total_amount), "paid")
                        print("\n<<<<<<<<<<<<<<<<< Thank You! >>>>>>>>>>>>>>>>>>")
                        logout = input("| Press x to logout |\n")

                        if logout == "x":
                            home()




def access(username=None, password=None):
    global data
    username = input("Enter your username:")
    password = input("Enter your password:")

    if not len(username or password) < 1:
        if True:
            database = open("registration.txt", "r")
            d = []
            f = []
            for i in database:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if username in data:
                    hashed = data[username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(password.encode(), hashed):
                            print("Login success!\n")
                            print("******************************************")
                            print(" Hi", username, ", Welcome To Car Rental System! \n")
                            dashboard()

                        else:
                            print("Wrong password")
                            access()

                    except:
                        print("Incorrect passwords or username")
                        access()
                else:
                    print("Username doesn't exist")
                    access()
            except:
                print("Password or username doesn't exist")
                access()
        else:
            print("Error logging into the system")
            access()
    else:
        print("Please attempt login again")
        access()




def signup(username=None, password1=None, password2=None):
    username = input("Enter a username:")
    password1 = input("Create password :")
    password2 = input("Confirm password:")
    database = open("registration.txt", "r")
    d = []
    for i in database:
        a, b = i.split(" ")
        b = b.strip()
        c = a, b
        d.append(a)

    if not len(password1) <= 8:
        database = open("registration.txt", "r")
        if not username is None:
            if len(username) < 1:
                print("Please provide a username")
                signup()
            elif username in d:
                print("Username exists")
                signup()
            else:
                if password1 == password2:
                    password1 = password1.encode('utf-8')
                    password1 = bcrypt.hashpw(password1, bcrypt.gensalt())
                    database = open("registration.txt", "a")
                    database.write(username+ ", " +str(password1)+ "\n")
                    print("Signup successful!")
                    print("| Press 0 to proceed to login |")



                else:
                    print("Passwords do not match")
                    signup()

    else:
        print("Password too short")
        signup()

def admin(choice=None):
    print("<<<<<<<<<<<<<<<<< ADMIN LOGIN >>>>>>>>>>>>>>>>>>")
    print("| Press 1 to Login |")
    file = open("admin.txt", "r")
    append = open("admin.txt", "a")
    choice = input()
    if choice == "1":
        Username_list = []
        Password_list = []
        for lines in file:
            lines = lines.rstrip()
            temp_list = lines.split()
            Username_list.append(temp_list[0])
            Password_list.append(temp_list[1])
            Username = input("Username: ")
            Password = input("Password: ")
            if Username not in Username_list:
                print("Incorrect username.")
                admin()
            if Password not in Password_list:
                print("Incorrect password.")
                admin()
            else:
                print("Login success!")
                file = open("rental.txt", "r")
                append = open("rental.txt", "a")
                print("\n\n\n*************************************************")
                print("Hello Admin", Username,"!")
                print("Details to update:\n")
                car = input(">Car available to be rented:")
                amount = input(">Rental pricing per day:")
                details = input(">Details of the car:")
                print("\n Confirm car details update?")
                print("| Yes (press y) | No (press n) |")
                choice = input()
                if choice == "y":
                    print("Car details update success!")
                    append.write("\n" + car + " " + amount + "Rs. " + details)
                elif choice == "n":
                    admin()



def user(choice=None):
    print("<<<<<<<<<<<<<<<<< USER LOGIN >>>>>>>>>>>>>>>>>>")
    print("| Press 0 to Login | Press 1 to Signup |")
    choice = input()
    if choice == "0":
        access()
    elif choice == "1":
        signup()

def home(choice=None):
    print("<<<<<<<<<<<<<< Car Rental System >>>>>>>>>>>>>>")
    print("| Press 0 if you are ADMIN | Press 1 if you are USER |")
    choice = input()
    if choice == "0":
       admin()

    elif choice == "1":
        user()


home()



