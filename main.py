MAX_LINES = 4
MAX_BET = 100
MIN_BET = 20

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

def lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ");
        if lines.isdigit():
            Lines = int(lines);
            if MAX_LINES >= Lines and Lines > 0:
                break;
            else:
                print("Enter a valid number of lines.");
        else:
            print("Please enter a number.");
    return Lines;

def bet():
    while True:
        betAmount = input("Enter the bet amount $");
        if betAmount.isdigit():
            betAmount = float(betAmount);
            if MAX_BET >= betAmount >= MIN_BET:
                print("Your bet amount is: $" + str(betAmount));
                break;
            else:
                print(f"The bet amount must be between {MIN_BET} and {MAX_BET}.");
        else:
            print("Please enter a valid number.");
    return betAmount;


def main():
    balance = deposit()
    no_of_lines = lines()

    while True:
        bet_amount = bet()
        total_bet = bet_amount * no_of_lines;
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Your current balance is: ${balance}.");
        else:
            break;

    print(f"You are betting ${bet_amount} on {no_of_lines} lines. Your total bet is: ${bet_amount * no_of_lines}. Your current balance is: ${balance}.");

main()