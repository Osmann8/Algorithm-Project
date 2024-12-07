# seperate all the functions

# This function takes the neccesary informations from user
def get_information():
    ID = input("Enter your identification number: ")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    return ID, name, surname

def get_illness_information():
    deficient_protein = int(input("Enter the deficient factor protein's number: "))
    while deficient_protein not in [8, 9]:
        deficient_protein = int(input("Enter the deficient factor protein's number: "))
    deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood: "))
    while deficient_factor_protein_level >= 50 and deficient_factor_protein_level < 0:
        deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood: "))
    number_of_antibody = float(input("The amount of antibody in blood produced against factor medication (BU)"))
    severity = severity_of_disease()
    if severity == "moderate":
        number_of_bleeding = float(input("The number of bleeding in the past year: "))
        while number_of_bleeding < 0:
            number_of_bleeding = float(input("The number of bleeding in the past year: "))
    if decide_to_prophylaxis():
        weight = float(input("Please enter your weight: "))
        production_type_of_factor = input("Please enter (P/p/R/r) for the production type of factor "
                                          "medication to be used (Plasma-derived/Recombinant)")

    return deficient_protein, deficient_factor_protein_level, number_of_antibody, number_of_bleeding

def decide_to_prophylaxis():
    _,_, number_of_antibody, number_of_bleeding = get_illness_information()
    severity = severity_of_disease()

    if severity == "severe" and number_of_antibody == 0:
        return True
    elif severity == "moderate" and number_of_bleeding >= 3:
        return True
    else:
        return False

#Following function takes the severity of the disease
def severity_of_disease():
    factor_level = get_illness_information()
    if factor_level < 1:
        return "severe"
    elif factor_level >=1 and factor_level<=5:
        return "moderate"
    else:
        return "mild"

def print_taken_informations():
    personel_information = get_information()
    print(f"ID: {personel_information[0]}\nName: {personel_information[1]}\nSurname: {personel_information[2]}")
    deficient_protein =get_illness_information()





def main():
    print_taken_informations()


main()


