print("1-check bmi")
print("2-see previous bmi records")
option=(input("enter your option:"))
if option == "1":
    mass=int(input("enter your body mass in kg here: "))
    height=float(input("enter your body height in meters here: "))
    date=(input("enter the month here"))
    bmi=mass/(height*height)
    print(bmi)
    save=input("would you like to save the file")
    if save=="yes":
        file=open("bmi.txt", "a")
        file.write(f"\n  my bmi is {bmi} on {date}")
        file.close()
        print("your information has been saved")
    else:
        print("information was not saved")
else:
    file=open("bmi.txt", "r")
    oldRecords=file.read()
    file.close()
    print(oldRecords)