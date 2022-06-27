
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered 0, please enter valid number")
        else:
            print("-ve number, so no conversion needed")
    except ValueError:
        print("Your input in not a valid number, dont ruin my program")

