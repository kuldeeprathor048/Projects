#Project = 1 theatre ticket booking system
normal_seats = 130
recliner_seats = 20
while True:
    print("""
        normal seat price = 200
        recliner seat price = 300""")
    name = input("Please enter your name: ").upper()
    seat_type = input("which type of seat do you want to book?(normal/recliner): ")
        
    if seat_type == "recliner":
        seats = int(input("How many seats do you want to book? "))
        if seats <= recliner_seats:
            recliner_seats -= seats
            total = seats*300
        else:
            print("Housefull")
            print("Sorry, We have", recliner_seats, "seats left in recliner")
            continue


    elif seat_type == "normal":
        seats = int(input("How many seats do you want to book? "))
        if seats <= normal_seats:
            normal_seats -= seats
            total = seats*200
        else:
            print("Housefull")
            print("Sorry! We have", normal_seats, "seats left in normal")
            continue
    else:
        print("-"*50)
        print("   PLEASE READ CAREFULLY & CHOOSE CORRECT OPTION")
        continue
        
            
    combo = input("Do you want to add combo of Pop Corn and Cold drink of Rs. 150? (yes/no): ")

    if combo == "yes":
        quantity = int(input("How much combo do you want to add? "))
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
    print("Normal seats remaining: ", normal_seats) 
    print("Recliner seats remaining: ", recliner_seats)
    if repeat == "no":
        break
