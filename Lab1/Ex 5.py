m=int(input("month= "))

match m:
    case 1|3|5|7|8|10|12:
        print("this month has 31 days")
    case 2:
        y=int(input("y= "))
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            print("this month has 29 days")
        else:
            print("this month has 28 days")
    case _:
        print("this month has 30 days")