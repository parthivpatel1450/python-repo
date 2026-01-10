year=int(input("Enter a Year="))

if year%400==0:
    print("LeapYear")
elif year%4==0 and year%100!=0:
    print("LeapYear")
else:
    print("Not a LeapYear")