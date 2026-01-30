def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: $");
        if amount.isdigit():
            amount = float(amount);
            if amount > 0:
                print("You have deposited: $" + str(amount));
                break;
            else:
                print("The amount must be greater than zero.");
        else:
            print("Please enter a valid number.");
    return amount;

deposit();