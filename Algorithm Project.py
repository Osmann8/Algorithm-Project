# Take personel information
ID = input("Enter your identification number: ")
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Take information about protein and it's level
deficient_protein = int(input("Enter the deficient factor protein's number: "))
while deficient_protein not in [8, 9]:
    deficient_protein = int(input("Enter the deficient factor protein's number: "))
# Protein level in blood (%)
deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood: "))
while deficient_factor_protein_level >= 50 and deficient_factor_protein_level < 0:
    deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood: "))

number_of_antibody = float(input("The amount of antibody in blood produced against factor medication (BU)"))
if number_of_antibody < 0:
    number_of_antibody = float(input("The amount of antibody in blood produced against factor medication (BU)"))

#Severity
if deficient_factor_protein_level < 1:
    severity = "severe"
elif deficient_factor_protein_level>=1 and deficient_factor_protein_level<=5:
    severity = "moderate"
else:
    severity = "mild"

if severity == "moderate":
    #number of bleeding in the past year
    number_of_bleeding = int(input("Enter the number of bleeding in the past year: "))
    if number_of_bleeding < 0:
        number_of_bleeding = int(input("Enter the number of bleeding in the past year: "))
# Patients that will be included in prophylaxis program
prophylaxis = False
if (severity == "severe" and number_of_antibody == 0) or (severity == "moderate" and number_of_bleeding >= 3):
    weight = float(input("Enter your weight: "))
    factor_production_type = input("Enter (P/p/R/r) for the production type of factor"
                                   " medication to be used (Plasma-derived/Recombinant)")
    while factor_production_type not in ["P","p","R","r"]:
        factor_production_type = input("Enter (P/p/R/r) for the production type of factor"
                                       " medication to be used (Plasma-derived/Recombinant)")
    prophylaxis = True

print(f"ID: {ID} \nName:{name} \nSurname:{surname}")
if deficient_protein == 8:
    print(f"Hemophilia A {severity}")
else:
    print(f"Hemophilia B {severity}")
if prophylaxis:
    print("The patient will be included in prophylaxis. Here are the informations:")
    if factor_production_type in ["P","p"]:
        factor_production_type = "Plasma-derived"
    else:
        factor_production_type = "Recombinant"

    # Factor medication to use
    print(f"The factor medication to be used: factor-{deficient_protein}/{factor_production_type}")
    # Medication period
    if deficient_protein == 8:
        print(f"3 times a week  to use the medication")
    else:
        print(f"2 times a week  to use the medication")

    # Minimum required dose of medication at one time  | %'yi mi hesaplıyoruz emin değilim
    minimum_required_dose_percentage = 40 - deficient_factor_protein_level
    if deficient_protein == 8:
        if minimum_required_dose_percentage % 2 == 0:
            minimum_dose_medication = (minimum_required_dose_percentage/2) * weight
        else:
            minimum_dose_medication = (minimum_required_dose_percentage+1)/2 * weight
    else:
        minimum_dose_medication = minimum_required_dose_percentage * weight
    print(f"Minimum required dose of medication at one time is: %{minimum_dose_medication}")

    # Amount of medication to be used at one time (IU), types and quantities of vials

    # name this a with apropriate name
    a = minimum_dose_medication / 250
    amount_of_total_medication = 0
    dose_2000, dose_1500, dose_1000, dose_500, dose_250 = 0, 0, 0, 0, 0
    while a > 0:
        remaining_required_dose = minimum_dose_medication
        vials_list = [250,500,1000,1500,2000]
        a = minimum_dose_medication / 250
        if a >= 2:
            if a>=4:
                if a>=6:
                    if a>=8:
                        minimum_dose_medication -= 2000
                        dose_2000 += 1
                        amount_of_total_medication += 2000
                    else:
                        minimum_dose_medication -= 1500
                        dose_1500 += 1
                        amount_of_total_medication += 1500
                else:
                    minimum_dose_medication -= 1000
                    dose_1000 += 1
                    amount_of_total_medication += 1000
            else:
                minimum_dose_medication -= 500
                dose_500 +=1
                amount_of_total_medication += 500
        elif a > 0 and a < 2:
            minimum_dose_medication -= 250
            amount_of_total_medication += 250
            dose_250 += 1
    print(f"Amount of medication to be used: {amount_of_total_medication}\n")
    if dose_250 > 0:
        print(f"{dose_250} vial of 250 ", end="")
        if dose_1000 or dose_500 or dose_2000 or dose_1500:
            print(",", end="")
    if dose_500 >0:
        print(f"{dose_500} vial of 500 ", end="")
        if dose_1000 or dose_2000 or dose_1500:
            print(",", end="")
    if dose_1000 > 0:
        print(f"{dose_1000} vial of 1000 ", end="")
        if dose_2000 or dose_1500:
            print(",", end="")
    if dose_1500 > 0:
        print(f"{dose_1500} vial of 1500 ", end="")
        if dose_2000 :
            print(",", end="")
    if dose_2000 > 0:
        print(f"{dose_2000} vial of 2000 ", end="")

    # Total amount of medication for 4 weeks, types and amounts of vials
    total_amount_medication_for_month = 0
    if deficient_protein == 8:
        total_amount_medication_for_month = amount_of_total_medication * 12





















