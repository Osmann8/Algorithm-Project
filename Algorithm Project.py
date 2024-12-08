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
    vial_sizes = [2000, 1500, 1000, 500, 250]
    vials_used = []
    for vial in vial_sizes:
        count = minimum_dose_medication / vial
        if int(count) > 0:
            if vial == 250:
                if count != int(count):
                    minimum_dose_medication -= (int(count) + 1) * vial
                    vials_used.append((vial, int(count) + 1))
                else:
                    vials_used.append((vial, int(count)))
                    minimum_dose_medication -= int(count) * vial
            else:
                vials_used.append((vial, int(count)))
                minimum_dose_medication -= int(count) * vial
    total_amount_medication = sum([vial * count for vial, count in vials_used])
    print(f"Amount of medication to be used at one time:{total_amount_medication}\n"
          f"Used vial types and quantities: ")
    for vial, count in vials_used:
        print(f"{count} vial of {vial}")

    # Total amount of medication for 4 weeks, types and quantities of vials
    total_medication_for_month = 0
    if deficient_protein == 8:
        total_medication_for_month += total_amount_medication * 12
        print(f"Total amount for 4 weeks: {total_medication_for_month}.\n"
              f"Used vials and quantities:")
        for vial, count in vials_used:
            print(f"{count*12} vial of {vial}")

    elif deficient_protein == 9:
        total_medication_for_month += total_amount_medication * 8
        print(f"Total amount for 4 weeks: {total_medication_for_month}.\n"
              f"Used vials and quantities:")
        for vial, count in vials_used:
            print(f"{count * 8} vial of {vial}")

    # Total medication cost for 4 weeks
    if factor_production_type in ["P","p"]:
        total_medication_cost = total_medication_for_month * 0.3
        print(f"Total medication cost for 4 weeks: {total_medication_cost}")
    elif factor_production_type in ["R","r"]:
        total_medication_cost = total_medication_for_month * 0.4
        print(f"Total medication cost for 4 weeks: {total_medication_cost}")































