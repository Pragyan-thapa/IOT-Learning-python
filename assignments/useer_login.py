user_name = "aman"
password = "12345"
entry = False
while not entry:
    user_input_user = input("Username: ")
    user_pass = input("Password: ")

    if user_input_user == user_name and user_pass == password:
        print("WELCOME")
        entry = True
    else:
        print("invalid userename or password")
        entry = False