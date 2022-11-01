#################################################################
# FILE : temperature.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex2 2023
# DESCRIPTION: Temperatue measurements and conclusions
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

def is_vormir_safe(min_temp, day1, day2, day3):
    """
    Making sure the temperature on Vormir is safe using measurements from 3 days
    min_temp - The threshold temperature
    day1, day2, day3 - Measurements from 3 consecutive days
    """
    unsafe_days = 0
    # Iterating over the measurements and counting days with lower-or-equal temperature to the minimal
    for day in [day1, day2, day3]:
        if day <= min_temp:
            unsafe_days += 1

    # If there is more than a single day with unsafe temperatures, Vormir is deemed UNSAFE.
    if unsafe_days > 1:
        return False
    else: # Vormir is safe
        return True    
