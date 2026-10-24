balance = 10000.00

print("Welcome to Kiran Bank")
print("Opening Balance: Rs.", int(balance))

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: Rs.", int(balance))

    elif choice == "2":
        try:
            deposit = float(input("Enter deposit amount: "))

            if deposit > 0:
                balance += deposit
                print("Deposit successful.")
                print("Updated Balance: Rs.", balance)
            else:
                print("Invalid amount! Amount must be greater than zero.")

        except ValueError:
            print("Invalid amount! Please enter a number.")

    elif choice == "3":
        try:
            withdrawal = float(input("Enter withdrawal amount: "))

            if withdrawal <= 0:
                print("Invalid amount! Amount must be greater than zero.")

            elif withdrawal <= balance:
                balance -= withdrawal
                print("Withdrawal successful.")
                print("Updated Balance: Rs.", balance)

            else:
                print("Transaction failed! Insufficient balance.")

        except ValueError:
            print("Invalid amount! Please enter a number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")
