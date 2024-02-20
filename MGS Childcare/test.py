workers_list = []
while True:
    answer = input("Would you like to enter a result (y to enter $ to exit): ")
    print("")
    if answer.lower() == "y":
        name = input("Staff Name: ")
        days_absent = int(input("Days Absent: "))
        print("")
        workers_list.append([name, days_absent])
    elif answer == "$":
        break
    else:
        print("Please input a valid answer\n")

most_absent_days = max([worker[1] for worker in workers_list])
most_abs = [worker for worker in workers_list if worker[1] == most_absent_days]


def list_cleaner(unclean):
    return [[word.strip('\' ,') for word in sublist] for sublist in unclean]


workers_list = list_cleaner(workers_list)


def avg_num_days(lst):
    total = sum([staff[1] for staff in lst])
    staff_amt = len(lst)
    avg = total / staff_amt
    return avg


average = round(avg_num_days(workers_list), 2)
above_avg = [worker for worker in workers_list if worker[1] > average]
no_abs = [worker for worker in workers_list if worker[1] == 0]

print("All workers:")
for worker in workers_list:
    print(worker)
print(f"The average amount of absences was {average}")
print(f"The most absences was {most_abs} with {most_absent_days} absences")
print("The people above the average amount of absences:")
for worker in above_avg:
    print(worker)
print("The People with no absences:")
for worker in no_abs:
    print(worker)
