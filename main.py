"""
COIN COUNTER PROJECT
""" 

print("Program to count coins and calculate values")
mixed_coins = input("Enter coin string: ")

penny = [0.01,  mixed_coins.count("p")]
nickel = [0.05,  mixed_coins.count("n")]
dime = [0.10, mixed_coins.count("d")]
quarter = [0.25, mixed_coins.count("q")]
half_dollar = [0.50, mixed_coins.count("h")]

total = penny[0] * penny[1] \
      + nickel[0] * nickel[1] \
      + dime[0] * dime[1] \
      + quarter[0] * quarter[1] \
      + half_dollar[0] * half_dollar[1]

report = (
        f"\n=====================================================\n"
        f"                Coin Counter Report\n"
        f"=====================================================\n\n"
        f"Coin          Value     Number    Amount \n"
        f"=====         ======    ======    ====== \n"
        f"Pennies       ${penny[0]}      {penny[1]}        $ {penny[0] * penny[1]} \n"
        f"Nickels       ${nickel[0]}      {nickel[1]}        $ {nickel[0] * nickel[1]} \n"
        f"Dimes         ${dime[0]}       {dime[1]}        $ {dime[0] * dime[1]} \n"
        f"Quarters      ${quarter[0]}      {quarter[1]}        $ {quarter[0] * quarter[1]} \n"
        f"Half-dollars  ${half_dollar[0]}       {half_dollar[1]}        $ {half_dollar[0] * half_dollar[1]} \n"
        f"                Total amount:     $ {total}                          \n"
    )

print(report)
