def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"

    number = ""

    while not number:

        try:

            number = int(input(question))

            return number

        except ValueError:

            print(error)


cars = [[1, "Suzuki Van", 2], [2, "Toyota Corolla", 4], [3, "Honda CRV", 4],
        [4, "Suzuki swift", 4], [5, "Mitsubishi Air-trek", 4],
        [6, "Nissan DC UTE", 4], [7, "Toyota Pre-via", 7],
        [8, "Toyota Hi Ace", 12], [9, "Toyota Hi Ace", 12]]

booked_list = []
while True:
    seats_needed = integer_checker("Please enter the number of seats "
                                   "required ("
                                   "enter"
                                   "-1 to quit): ")
    print("")
    if seats_needed == -1:
        break
    else:
        for car in cars:
            if seats_needed > car[2]:
                print(f"No.{car[0]} - {car[1]} - {car[2]} seats- "
                      f"Note: not enough space")
            else:
                print(f"No.{car[0]} - {car[1]} - {car[2]} seats- ")

        num_car = integer_checker("Enter a number to book: ") - 1
        name = input("Enter your name: ")
        booked_list.append([cars[num_car], name])
        print(f"{cars[num_car][1]} booked by {name}")

print("")
print("Vehicles booked today")
for car in booked_list:
    print(f"No. {car[0][0]} - {car[0][1]} - Booked by: {car[1]}")
