
print("CALCULATOR BELOW // TO EXIT ENTER: exit")
user_input = ""
while user_input != "exit":
    user_input = input("enter here: ")
    befor_operator = ""
    after_operator = ""
    
    if "+" in user_input:
        operator_index = user_input.index("+")
        for character in user_input[0:operator_index]:
            befor_operator += character
        
        for charactor_two in user_input[(operator_index+1):]:
            after_operator = after_operator + charactor_two

        try:
            number_one = int(befor_operator)
            number_two = int(after_operator)
            print("addition is:",number_one + number_two)
        except ValueError:
            print("Invalid input, please enter again")

                 
    elif "-" in user_input:
        operator_index = user_input.index("-")
        for character in user_input[0:operator_index]:
            befor_operator += character
        
        for charactor_two in user_input[(operator_index+1):]:
            after_operator = after_operator + charactor_two

        try:
            number_one = int(befor_operator)
            number_two = int(after_operator)
            print("subtraction is:",number_one - number_two)
        except ValueError:
            print("Invalid input, please enter again")
        
        
    elif "*" in user_input:
        operator_index = user_input.index("*")
        for character in user_input[0:operator_index]:
            befor_operator += character
        
        for charactor_two in user_input[(operator_index+1):]:
            after_operator = after_operator + charactor_two

        try:
            number_one = int(befor_operator)
            number_two = int(after_operator)
            print("multiplication is:",number_one * number_two)
        except ValueError:
            print("Invalid input, please enter again")
        

    elif "/" in user_input:
        operator_index = user_input.index("/")
        for character in user_input[0:operator_index]:
            befor_operator += character
        
        for charactor_two in user_input[(operator_index+1):]:
            after_operator = after_operator + charactor_two

        try:
            number_one = int(befor_operator)
            number_two = int(after_operator)
            print("division is:",number_one / number_two)
        except ValueError:
            print("Invalid input, please enter again")
        


    elif "%" in user_input:
        operator_index = user_input.index("%")
        for character in user_input[0:operator_index]:
            befor_operator += character
        
        for charactor_two in user_input[(operator_index+1):]:
            after_operator = after_operator + charactor_two

        try:
            number_one = int(befor_operator)
            number_two = int(after_operator)
            print("modulus is:",number_one % number_two)    
        except ValueError:
            print("Invalid input, please enter again")
        

    elif user_input=="exit":
        continue
    else:
        print("invalid input")

print("good bye")