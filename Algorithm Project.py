next_patient = True
# Take information about protein and it's level

total_patient = 0
number_of_hemo_A, number_of_hemo_B = 0, 0
number_of_severity_severe, number_of_severity_moderate, number_of_severity_mild  = 0, 0, 0
number_of_inhibitors_present_hemo_A, number_of_inhibitors_present_hemo_B = 0, 0



while next_patient:
    # Get personel informations
    ID = input("Enter patient's identification number: ")
    name = input("Enter patient's name: ")
    surname = input("Enter patient's surname: ")

    # Information about disease
    deficient_protein = int(input("Enter the deficient factor protein's number (8 or 9): "))
    while deficient_protein not in [8, 9]:
        deficient_protein = int(input("Enter the deficient factor protein's number (8 or 9): "))

    # Protein level in blood (%)
    deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood (0-49): "))
    while deficient_factor_protein_level >= 50 or deficient_factor_protein_level < 0:
        deficient_factor_protein_level = float(input(f"Factor-{deficient_protein} level in blood (0-49): "))

    number_of_antibody = float(input("The amount of antibody in blood produced against factor medication (BU): "))
    if number_of_antibody < 0:
        number_of_antibody = float(input("The amount of antibody in blood produced against factor medication (BU): "))
    if number_of_antibody > 0:
        if deficient_protein == 8:
            number_of_inhibitors_present_hemo_A +=1
        else:
            number_of_inhibitors_present_hemo_B += 1

    #Severity
    if deficient_factor_protein_level < 1:
        severity = "severe"
        severity_severe += 1
    elif deficient_factor_protein_level>=1 and deficient_factor_protein_level<=5:
        severity = "moderate"
        severity_moderate += 1
    else:
        severity = "mild"
        severity_mild += 1

    if severity == "moderate":
        #number of bleeding in the past year
        number_of_bleeding = int(input("Enter the number of bleeding average per month in the past year: "))
        if number_of_bleeding < 0:
            number_of_bleeding = int(input("Enter the number of bleeding in the past year: "))
    # Patients that will be included in prophylaxis program
    prophylaxis = False
    if (severity == "severe" and number_of_antibody == 0) or (severity == "moderate" and number_of_bleeding >= 3):
        print("-->The patient will be included in prophylaxis.")
        weight = float(input("Enter the patient's weight: "))
        factor_production_type = input("Enter (P/p/R/r) for the production type of factor"
                                       " medication to be used (Plasma-derived/Recombinant): ")
        while factor_production_type not in ["P","p","R","r"]:
            factor_production_type = input("Enter (P/p/R/r) for the production type of factor"
                                           " medication to be used (Plasma-derived/Recombinant): ")
        prophylaxis = True

    print(f"ID: {ID} \nName:{name} \nSurname:{surname}")
    if deficient_protein == 8:
        print(f"Type of disease: Hemophilia A, severity: {severity}")
        number_of_hemo_A += 1
    else:
        print(f"Hemophilia B {severity}")
        number_of_hemo_B += 1
    if prophylaxis:
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
        print(f"Minimum required dose of medication at one time is: {minimum_dose_medication}")

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
              f"Used vial types and quantities at one time: ")
        for vial, count in vials_used:
            print(f"    {count} vial of {vial}")

        # Total amount of medication for 4 weeks, types and quantities of vials
        total_medication_for_month = 0
        if deficient_protein == 8:
            total_medication_for_month += total_amount_medication * 12
            print(f"Total amount for 4 weeks: {total_medication_for_month}\n"
                  f"Used vials and quantities:")
            for vial, count in vials_used:
                print(f"    {count*12} vial of {vial}")

        elif deficient_protein == 9:
            total_medication_for_month += total_amount_medication * 8
            print(f"Total amount for 4 weeks: {total_medication_for_month}\n"
                  f"Used vials and quantities:")
            for vial, count in vials_used:
                print(f"    {count * 8} vial of {vial}")

        # Total medication cost for 4 weeks
        if factor_production_type in ["P","p"]:
            total_medication_cost = total_medication_for_month * 0.3
            print(f"Total medication cost for 4 weeks: {total_medication_cost}")
        elif factor_production_type in ["R","r"]:
            total_medication_cost = total_medication_for_month * 0.4
            print(f"Total medication cost for 4 weeks: {total_medication_cost}")
    else:
        print("Prophylaxis won't be provided")


    next_patient = input("Are there next patient? (Y/y/N/n): ")
    while next_patient not in ["Y","y","N","n"]:
        next_patient = input("Are there next patient? (Y/y/N/n): ")
    if next_patient in ["Y","y"]:
        next_patient = True
    else:
        next_patient = False

    total_patient += 1

# Search it if total_patient is necessary or not. (hemo_a + hemo_b can be used)
print(f"Number of Hemophilia-A: {number_of_hemo_A}\nNumber of Hemophilia-B: {number_of_hemo_B}"
      f"\nNumber of all patients: {total_patient}")

# Numbers and percentages of patients with severe, moderate and mild hemophilia
percentage_of_severe_patients = number_of_severity_severe * 100 / total_patient
percentage_of_moderate_patients = number_of_severity_moderate * 100 / total_patient
percentage_of_mild_patients = number_of_severity_mild * 100 / total_patient
print(f"Number of patients with severe hemophilia: {number_of_severity_severe} and percentage: {percentage_of_severe_patients}")
print(f"Number of patients with moderate hemophilia: {number_of_severity_moderate} and percentage: {percentage_of_moderate_patients}")
print(f"Number of patients with severe hemophilia: {number_of_severity_mild} and percentage: {percentage_of_mild_patients}")

# Percentages of inhibitor presence in Hemophilia-A and Hemophilia-B patients individually
inhib_presence_A_percentage = number_of_inhibitors_present_hemo_A * 100 / number_of_hemo_A
inhib_presence_B_percentage = number_of_inhibitors_present_hemo_B * 100 / number_of_hemo_B
print(f"Percentage of inhibitor presence in Hemophilia-A: {inhib_presence_A_percentage}")
print(f"Percentage of inhibitor presence in Hemophilia-B: {inhib_presence_B_percentage}")






