#Cube of a number
while True:
    try:
        nbr = float(input("Now enter a number: "))       
    except ValueError:
        print("Have a look at this: https://en.wikipedia.org/wiki/Number")
        continue
    else:
        print ("The cube of ", nbr, "is", nbr*nbr*nbr)
        break 
