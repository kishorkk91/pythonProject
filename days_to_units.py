# print("20 days are " + str(50) + " minutes")

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered 0, please enter valid number")
        else:
            print("-ve number, so no conversion needed")
    except ValueError:
        print("Your input in not a valid number, dont ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Heyy user, enter number of days! \n")
    for num_of_days_element in set(user_input.split(",")):
        validate_and_execute()

