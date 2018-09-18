# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future
#    Worked with Chris Gallevo.

def main():
    year = eval(input("Enter the years of investment: "))
    print("This program calculates the future value")
    print("of a",year,'- year investment.')

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    comp = eval(input("Enter the number of compounding periods: "))
    total_amt = -principal
    principal = int(principal)
    apr = float(apr)
    comp = int(comp)
    y = int(year)
    for i in range(y+1):
        total_amt = total_amt + principal*(1 + apr/comp)**(i*comp)
        print(total_amt)
            
    print("The value in",year,"year(s) is:",total_amt)
    main()


main()
