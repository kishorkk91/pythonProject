from helper import validate_and_execute
import logging

logger = logging.getLogger("MAIN")
logger.error("Error test")

user_input = ""
while user_input != "exit":
    user_input = input("Heyy user, enter number of days and conversion unit! \n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)
