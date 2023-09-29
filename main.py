"""
COIN COUNTER PROJECT
Author: Kaypee90
"""

from collections import namedtuple

def main():
    """
    Coins counter program
    """
    print("Program to count coins and calculate values")
    mixed_coins = input("Enter coin string: ") # Example pppnnndddqqqh

    coin = namedtuple("Coin", ["Value", "Quantity", "SubTotal"])

    penny = coin(0.01, mixed_coins.count("p"), 0.01 * mixed_coins.count("p"))
    nickel = coin(0.05, mixed_coins.count("n"), 0.05 * mixed_coins.count("n"))
    dime = coin(0.10, mixed_coins.count("d"), 0.10 * mixed_coins.count("d"))
    quarter = coin(0.25, mixed_coins.count("q"), 0.25 * mixed_coins.count("q"))
    half_dollar = coin(0.50, mixed_coins.count("h"), 0.50 * mixed_coins.count("h"))

    total = (
        penny.SubTotal
        + nickel.SubTotal
        + dime.SubTotal
        + quarter.SubTotal
        + half_dollar.SubTotal
    )

    report = (
        f"\n=====================================================\n"
        f"                Coin Counter Report\n"
        f"=====================================================\n\n"
        f"Coin          Value     Number    Amount \n"
        f"=====         ======    ======    ====== \n"
        f"Pennies       ${penny.Value}      {penny.Quantity}        $ {penny.SubTotal} \n"
        f"Nickels       ${nickel.Value}      {nickel.Quantity}        $ {nickel.SubTotal} \n"
        f"Dimes         ${dime.Value}       {dime.Quantity}        $ {dime.SubTotal} \n"
        f"Quarters      ${quarter.Value}      {quarter.Quantity}        $ {quarter.SubTotal} \n"
        f"Half-dollars  ${half_dollar.Value}       {half_dollar.Quantity}        $ {half_dollar.SubTotal} \n"
        f"                Total amount:     $ {total}                          \n"
    )

    print(report)

if __name__ == "__main__":
    main()
