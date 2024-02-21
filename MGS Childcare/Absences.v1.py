workers_list = []
most_abs = []
while True:
    answer = input("Would you like to enter a result (y to enter $ to "
                   "exit):")
    print("")
    if answer == "y" or answer == "Y":
        ID = [input("Staff Name:"), int(input("Days Absent:"))]
        print("")
        for i in range(0, 1):
            workers_list.append(ID)
    elif answer == "$":
        break
    else:
        print("please input a valid answer\n")
# help from ChatGPT(17, 18)
most_absent_days = max([worker[1] for worker in workers_list])
most_abs = [worker for worker in workers_list if worker[1] == most_absent_days]


def avg_num_days(lst):
    total = 0
    staff_amt = int(len(lst))
    for staff in lst:
        total += staff[1]
    avg = total / staff_amt
    return avg


average = round(avg_num_days(workers_list), 2)
# help from ChatGPT (32)
above_avg = [worker for worker in workers_list if worker[1] > average]

no_abs = [worker for worker in workers_list if worker[1] == 0]

print("All workers:")
for worker in workers_list:
    print(' '.join(map(str, worker)))
print(f"The average amount of absences was {average}")
print(f"The most absences was {' '.join(map(str, most_abs))} with"
      f" {' '.join(map(str, most_absent_days))} absences")
print("The people above the average amount of absences:")
for worker in above_avg:
    print(' '.join(map(str, worker)))
print("The People with no absences:")
for worker in no_abs:
    print(' '.join(map(str, worker)))
