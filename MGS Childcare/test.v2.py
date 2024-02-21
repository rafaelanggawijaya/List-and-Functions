def calcu_fines(speeds):
    if speeds < 10:
        return 30
    elif 10 <= speeds <= 14:
        return 80
    elif 15 <= speeds <= 19:
        return 120
    elif 20 <= speeds <= 24:
        return 170
    elif 25 <= speeds <= 29:
        return 230
    elif 30 <= speeds <= 34:
        return 300
    elif 35 <= speeds <= 39:
        return 400
    elif 40 <= speeds <= 44:
        return 510
    else:
        return 630


number_offenders = 0
total_fines = 0
arrests = ["James Wilson", "Helga Norman",
           "Zachary Conroy"]
offenders = []
while True:
    answer = input("Would you like to add an offender (y/n):").lower()
    print("")
    if answer == "y":
        speeder_name = input("Enter offender's name:").title()
        speeder_speed = int(input("Enter the amount the offender exceeded:"))
        if speeder_name in arrests:
            print(f"{speeder_name} - WARRANT TO ARREST -")
        fined = calcu_fines(speeder_speed)
        print(f"{speeder_name} is to be fined ${fined}")
        number_offenders += 1
        offenders.append([number_offenders, speeder_name, speeder_speed, fined])
        total_fines += fined
        print("")
    elif answer == "n":
        break
    else:
        print("Please enter a valid answer")

print(f"Total fines: {total_fines}\n")
for offender in offenders:
    print(f"{offender[0]}) {offender[1]} Amount over the limit: {offender[2]}")
print(f"The total amount fined was ${total_fines}")
