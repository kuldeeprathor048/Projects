#Project = 1 theatre ticket booking system
normal_seats = 0
recliner_seats = 0
total = 0
seats = 0
while True:
    print("""
        normal seat price = 200
        recliner seat price = 300""")
    name = input("Please enter your name: ").upper()
    type = input("which type of seat do you want to book?(normal/recliner): ")
    while True:
        
        if type == "recliner":
            seats = int(input("How many seats do you want to book? "))
            recliner_seats += seats
            if recliner_seats <= 20:
                total = seats*300
            
            
            if recliner_seats > 20:
                print("Housefull")
                recliner_seats -= seats
                print("Seats remaining: ", 20 - recliner_seats)
            repeat = input("do yo want to choose again? (yes/no): ")
            recliner_seats + seats
            if repeat == "no":
                break
            
        
        elif type == "normal":
            seats = int(input("How many seats do you want to book? "))
            normal_seats += seats
            if normal_seats <= 130:
                total = seats*200
            
            if normal_seats > 130:
                print("Housefull")
                normal_seats -= seats
                print("Seats remaining: ", 130 - normal_seats)
            repeat = input("do yo want to choose again? (yes/no): ")
            if repeat == "no":
                break
    else:
        print("-"*50)
        print("   PLEASE READ CAREFULLY & CHOOSE CORRECT OPTION")

        
            
    combo = input("Do you want to add combo of Pop Corn and Cold drink of Rs. 150? (yes/no): ")

    if combo == "yes":
        quantity = int(input("How much combo do you want to add? "))
        if quantity >= 1:
            combo_price = quantity*150
            total = total+combo_price
        print("-"*40)
        print(name, "Your Total amount is =",total)
        print("       THANK YOU")
        print("-"*40)
    else:
        print("-"*40)
        print(name, "Your Total amount is =", total)
        print("       THANK YOU")
        print("-"*40)


    repeat = input("Go to next person? (yes/no): ")
    print("Normal seats remaining: ", 130 - normal_seats) 
    print("Recliner seats remaining: ", 20 - recliner_seats)
    if repeat == "no":
        break
