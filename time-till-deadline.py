from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon Ex: --> python:09.01.2023 \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)

# calculate how many days from now till deadline

current_date = datetime.today()

hours_till = deadline_date - current_date

print(f"Dear user! Time remaining for your goal: {goal} are {int(hours_till.total_seconds()/60/60)} hours")
