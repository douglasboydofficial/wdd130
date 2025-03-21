# Import datetime to use it to calculate person's age
from datetime import datetime

def main ():
    """Get the user's gender, birthdate, height, & weight.
    Calls the compute_age, kg_from_lb, cm_from_in, body_mass_index, &
    basal_metabolic_rate functions. Prints the results."""
    # Gets input
    gender = input ("Please enter your gender (M or F): ").upper()
    birthdate = input ("Enter your birthdate (YYYY-MM-DD): ")  
    weight = round (int (input ("Enter your weight in U.S. pounds: ")))
    height = round (int (input ("Enter your height in U.S. inches: ")))

    # calls the functions
    age = compute_age (birthdate)
    kg = kg_from_lb (weight)
    cm = cm_from_in (height)
    m = m_from_cm (cm)
    bmi = body_mass_index (kg, cm)
    BMR = basal_metabolic_rate (gender, kg, cm, age)
    
    # prints results for user to see
    print (f"Age (years): {age}")
    print (f"Weight (kg): {kg: .2f}")
    print (f"Height (m): {m: .2f}")
    print (f"Body mass index: {bmi}")
    print (f"Basal metabolic rate (kcal/day): {BMR}")


def compute_age (birthdate):
    """converts the birthdate string and converts it to a date type.
    Calculates to get an age from the date now and birthdate input. Returns
    results."""
    # stores birthdate as a date data type. Stores today's date.
    birthday = datetime.strptime (birthdate, "%Y-%m-%d")
    today = datetime.now()

    # Calculates a user's age.
    years = today.year - birthday.year

    # Pin points the person's age to the day.
    if birthday.month > today.month or \
        (birthday.month == today.month and \
            birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb (weight):
    """Converts a user's weight from pounds to kilograms. Returns the results."""
    kg = round (weight * 0.45359237, 2)

    return kg


def cm_from_in (height):
    """Converts a user's height from inches to centimeters. Returns the results."""
    cm = round (height * 2.54, 1)

    return cm


def m_from_cm (cm):
    """Converts a user's height from centimeters to meters. Returns the results."""
    m = cm / 100

    return m


def body_mass_index (kg, cm):
    """Calculates a person's body mass index. Returns the results."""
    #Body mass index equals (10,000 times kilograms) divided by (centimeters squared)
    bmi = round ((10000 * kg) / cm ** 2, 1)

    return bmi


def basal_metabolic_rate (gender, kg, cm, age):
    """Calculates a user's basal metabolic rate (BMR) based off the user's gender.
    Returns the results."""
    # A woman's BMR equals 447.593 plus 9.247 times weight (kg) plus 3.098 times height (cm) minus 4.330 times age.
    if gender == "F":
        bmr = round (447.593 + 9.247 * kg + 3.098 * cm - 4.330 * age)

    # A man's BMR equals 88.362 plus 13.397 times weight (kg) plus 4.799 times height (cm) minus 5.677 times age.
    elif gender == "M":
        bmr = round (88.362 +13.397 * kg + 4.799 * cm - 5.677 * age)

    return bmr


#Calls to main function
main()