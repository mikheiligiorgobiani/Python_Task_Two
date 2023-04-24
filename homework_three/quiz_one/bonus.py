number = str(input("please write number:"))
if int(number[-1]) / 2 % 1:
    print(f"this number is odd:{number}" )
else:
    print(f"this number is even:{number}")