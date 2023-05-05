def ticket(name,age):

    starting_destination=["BANGLORE","HYDERABAD"]
    print(starting_destination)
    while True:
        try:
            starting = input("Enter your starting destination : ")
            if starting in starting_destination:
                break
            break 
        except:
            print("You entered wrong starting point ")