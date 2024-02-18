num_trip = 0
total_cost_list = []
times = []
driver_name = input("Driver's name:").title()
print("")
while True:
    trip = input("Start new Trip (y/n):")
    if trip == "y" or trip == "Y":
        num_trip += 1
        time = float(input("How long is this trip (in minutes):"))
        cost = 10 + 2 * time
        times.append(time)
        total_cost_list.append(cost)
        print(f"This trip will cost ${cost}\n")
    elif trip == "n" or "N":
        print("")
        break
    else:
        print("Please enter a valid answer\n")
total_cost = sum(total_cost_list)
total_time = sum(times)
average_cost = total_cost / num_trip
average_time = total_time / num_trip
print(f"Driver {driver_name} had {num_trip} trip/s which "
      f"totalled at {total_time} minutes\nThe average time for "
      f"each trip was {average_time} minutes\n"
      f"The total income was ${total_cost}\n"
      f"The average cost of all trip/s was ${average_cost}")
