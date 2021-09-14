"""
Name: Lydia Heath
interest.py

Problem: Calculating monthly interest.

Certificate of Authenticity:
I certify this project is entirely my own.
"""


def main():
    annual_interest = eval(input("enter annual interest rate: "))
    billing_cycle = eval(input("enter number of days in billing cycle: "))
    net_balance = eval(input("enter balance: "))
    step_one = net_balance * billing_cycle
    net_payment = eval(input("enter payment amount: "))
    day_of_payment = (eval(input("enter day of payment: ")))
    end_cycle = billing_cycle - day_of_payment
    step_two = net_payment * end_cycle
    step_three = step_one - step_two
    step_four = step_three / billing_cycle
    monthly_interest = annual_interest / 12
    monthly_interest_charge = (step_four * monthly_interest) / 100
    print(round(monthly_interest_charge, 2))


if __name__ == '__main__':
    main()
