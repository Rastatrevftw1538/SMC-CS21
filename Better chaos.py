# File: chaos.py
# A simple program illustrating chaotic behavior.

def main(x):
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    chaos_list = []
    if x <= 1:
        for i in range(10):
            x = 3.9 * x * (1 - x)
            print(x)
            chaos_list.append(x)
            main()
            return chaos_list
    if x >= 0:
         for i in range(10):
            x = 3.9 * x * (1 - x)
            print(x)
            chaos_list.append(x)
            main()
    else:
        print("try again")
        chaos_list.append(x)
        main()

main(0.5)
