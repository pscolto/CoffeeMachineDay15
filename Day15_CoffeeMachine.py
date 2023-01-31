resource_report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100
}
drink_cost = {
            "espresso": 1.50,
            "latte": 2.50,
            "cappuccino": 3.00}


def espresso():
    if resource_report["Water"] >= 50:
        resource_report["Water"] = resource_report["Water"] - 50
    else:
        print("Not enough water to continue, goodbye")
        quit()
    if resource_report["Coffee"] >= 18:
        resource_report["Coffee"] = resource_report["Coffee"] - 18
    else:
        print("Not enough coffee to continue, goodbye")
        quit()
    print(resource_report)



def latte():
    if resource_report["Water"] >= 200:
        resource_report["Water"] = resource_report["Water"] - 200
    else:
        print("Not enough water to continue, goodbye")
        quit()
    if resource_report["Coffee"] >= 24:
        resource_report["Coffee"] = resource_report["Coffee"] - 24
    else:
        print("Not enough coffee to continue, goodbye")
        quit()
    if resource_report["Milk"] >= 150:
        resource_report["Milk"] = resource_report["Milk"] - 150
    else:
        print("Not enough milk to continue, goodbye")
        quit()
    print(resource_report)



def cappuccino():
    if resource_report["Water"] >= 250:
        resource_report["Water"] = resource_report["Water"] - 250
    else:
        print("Not enough water to continue, goodbye")
    if resource_report["Coffee"] >= 24:
        resource_report["Coffee"] = resource_report["Coffee"] - 24
    else:
        print("Not enough coffee to continue, goodbye")
    if resource_report["Milk"] >= 100:
        resource_report["Milk"] = resource_report["Milk"] - 100
    else:
        print("Not enough milk to continue, goodbye")
    print(resource_report)



def coffee_choice():
    choice1 = input("What would you like? Press 'Q' to quit or 'espresso', 'latte', 'cappuccino' or 'report': ").lower()
    if choice1 == "report":
        print(resource_report)
        coffee_choice()
    elif choice1 == "espresso":
        espresso()
    elif choice1 == "latte":
        latte()
    elif choice1 == "cappuccino":
        cappuccino()
    elif choice1 == "q":
        print("Goodbye")
        exit()
    else:
        print("invalid input, only enter name of drink or 'report' or 'Q', ty")
    did_they_pay = False
    total_inserted = 0
    while did_they_pay is False:
        print(f"{choice1} costs {drink_cost[choice1]}")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total_inserted += (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
        print(f"Total inserted = {total_inserted}")
        if total_inserted >= drink_cost[choice1]:
            print(f"Enjoy your {choice1}!")
            print("""
                                    (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      ""--..__                              __..--""/
       '._     ""----.....______.....----""     _.'
          `""--..,,_____            _____,,..--""`
                        `""----""`
            """)
            print(f"Your change is {total_inserted - drink_cost[choice1]}")
            coffee_choice()


coffee_choice()
