#ATM PIN = 1234
Balance = 100
pin = int(input("Enter ATM PIN: "))
if pin == 1234:
    print("Welcome")


    while True:
        ATM = input("Enter Your choice: ")
        match ATM:
            case"1":   # WITHDRAW MONEY
                amount = int(input("Enter the amount you want to withdrawl: "))
                if amount <= 0:
                    print("Please enter a valid amount")
                elif amount <= Balance:
                    Balance -= amount
                    print("Withdrawl of", amount, "is successful" )
                    print("Current Balance", Balance)
                else:
                    print("Insufficient Balance")
            case"2":   # DEPOSIT MONEY
                amount = int(input("Enter the amount you want to deposit"))
                if amount <=0:
                    print("Please enter a valid amount")
                else:
                    Balance = Balance + amount
                    print("Deposit of", amount, "is successful")
                    print("Current Balance", Balance)
            case"3":     # CHECK BALANCE
                print("Current balance",Balance)
            case"4":    # EXIT
              break
            case _:
                print("Invalid Choice")
else:
    print("Invalid PIN")                

# -- USER FRIENDLY 1,2,3== COMMENT done 
# -- LOOP FEATURE; LOOP ADD TILL USER EXIT done 
# -- EDGE CASE  done
# -- ATM PIN USER WILL INPUT -- IF ELSE THEN ONLY ATM KA OPENS  done


# RANDINT USER LEVEL ATM PIN  {Understand this conept and then execute} 
