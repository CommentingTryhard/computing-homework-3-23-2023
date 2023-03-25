#Q2

lists = [0,1,2,3,4,5,6]

ans = int(input("Please input le numba: "))
if ans in lists:
    if ans == 0:
        print("Monday")
    elif ans == 1:
        print("Tuesday")
    elif ans == 2:
        print("Wednesday")
    elif ans == 3:
        print("Thursday")
    elif ans == 4:
        print("Friday")
    elif ans == 5:
        print("Saturday")
    elif ans == 6:
        print("Sunday")
else:
    print("Error!!")
