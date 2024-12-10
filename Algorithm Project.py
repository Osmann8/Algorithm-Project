next_patient = True

total_patient = 0
# hemophilia-a ve b'ye sahip olan hasta sayıları
number_of_hemo_A, number_of_hemo_B = 0, 0
number_of_severity_severe, number_of_severity_moderate, number_of_severity_mild  = 0, 0, 0
number_of_inhibitors_present_hemo_A, number_of_inhibitors_present_hemo_B = 0, 0
# Prophylaxis alan hemophilia-a ve hemophilia-b'lerin sayısı
number_of_patients_receiving_prophylaxis_A, number_of_patients_receiving_prophylaxis_B = 0, 0
# Moderate olarak prophylaxis'e girmiş olanların sayısı
number_of_prophylaxis_with_severity_moderate = 0

while next_patient:
    # Get personel informations
    ID = input("Enter patient's identification number: ")
    name = input("Enter patient's name: ")
    surname = input("Enter patient's surname: ")

    # Deficient protein type
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
        number_of_severity_severe += 1
    elif deficient_factor_protein_level>=1 and deficient_factor_protein_level<=5:
        severity = "moderate"
        number_of_severity_moderate += 1
    else:
        severity = "mild"
        number_of_severity_mild += 1

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
        if severity == "moderate":
            number_of_prophylaxis_with_severity_moderate += 1
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
            number_of_patients_receiving_prophylaxis_A += 1
        else:
            print(f"2 times a week  to use the medication")
            number_of_patients_receiving_prophylaxis_B += 1

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
        a = minimum_dose_medication / 250
        amount_of_total_medication = 0
        dose_2000, dose_1500, dose_1000, dose_500, dose_250 = 0, 0, 0, 0, 0
        while a > 0:
            remaining_required_dose = minimum_dose_medication
            a = minimum_dose_medication / 250
            if a > 7:
                dose_2000 += 1
                minimum_dose_medication -= 2000
                amount_of_total_medication += 2000
            elif a > 5 and int(a) <= 7:
                dose_1500 += 1
                minimum_dose_medication -= 1500
                amount_of_total_medication += 1500
            elif a > 3 and int(a) <= 5:
                dose_1000 += 1
                minimum_dose_medication -= 1000
                amount_of_total_medication += 1000
            elif a > 1 and int(a) <= 3:
                dose_500 += 1
                minimum_dose_medication -= 500
                amount_of_total_medication += 500
            elif a > 0 and int(a) <= 1:
                dose_250 += 1
                minimum_dose_medication -= 250
                amount_of_total_medication += 250

        print(f"Amount of medication to be used: {amount_of_total_medication}. Type and quantities of vials: ", end="")
        if dose_250 > 0:
            print(f"{dose_250} vial of 250 IU", end="")
            if dose_1000 or dose_500 or dose_2000 or dose_1500:
                print(",", end="")
            else:
                print()
        if dose_500 > 0:
            print(f"{dose_500} vial of 500 IU", end="")
            if dose_1000 or dose_2000 or dose_1500:
                print(",", end="")
            else:
                print()
        if dose_1000 > 0:
            print(f"{dose_1000} vial of 1000 IU", end="")
            if dose_2000 or dose_1500:
                print(",", end="")
            else:
                print()
        if dose_1500 > 0:
            print(f"{dose_1500} vial of 1500 IU", end="")
            if dose_2000:
                print(",", end="")
            else:
                print()
        if dose_2000 > 0:
            print(f"{dose_2000} vial of 2000 IU")

        # Total amount of medication for 4 weeks, types and quantities of vials
        total_medication_for_month = 0
        if deficient_protein == 8:
            total_medication_for_month += amount_of_total_medication * 12
            print(f"Total amount for 4 weeks: {total_medication_for_month} IU\n"
                  f"Used vials and quantities: ",end="" )
            # Bu işte bi yanlışlık var gibi ama :
            if dose_250 > 0:
                print(f"{dose_250} vial of 250 IU")
            if dose_500 > 0:
                print(f"{dose_500} vial of 500 IU")
            if dose_1000 > 0:
                print(f"{dose_1000} vial of 1000 IU")
            if dose_1500 > 0:
                print(f"{dose_1500} vial of 1500 IU")
            if dose_2000 > 0:
                print(f"{dose_2000} vial of 2000 IU")


        elif deficient_protein == 9:
            total_medication_for_month += amount_of_total_medication * 8
            print(f"Total amount for 4 weeks: {total_medication_for_month} IU\n"
                  f"Used vials and quantities:")
            if dose_250 > 0:
                print(f"{dose_250} vial of 250 IU")
            if dose_500 > 0:
                print(f"{dose_500} vial of 500 IU")
            if dose_1000 > 0:
                print(f"{dose_1000} vial of 1000 IU")
            if dose_1500 > 0:
                print(f"{dose_1500} vial of 1500 IU")
            if dose_2000 > 0:
                print(f"{dose_2000} vial of 2000 IU")

        # Total medication cost for 4 weeks
        if factor_production_type == "Plasma-derived":
            total_medication_cost = total_medication_for_month * 0.3
            print(f"Total medication cost for 4 weeks: {total_medication_cost}$")
        elif factor_production_type == "Recombinant":
            total_medication_cost = total_medication_for_month * 0.4
            print(f"Total medication cost for 4 weeks: {total_medication_cost}$")
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
print(f"Number of patients with severe hemophilia: {number_of_severity_severe} and percentage: {percentage_of_severe_patients}%")
print(f"Number of patients with moderate hemophilia: {number_of_severity_moderate} and percentage: {percentage_of_moderate_patients}%")
print(f"Number of patients with severe hemophilia: {number_of_severity_mild} and percentage: {percentage_of_mild_patients}%")

# Percentages of inhibitor presence in Hemophilia-A and Hemophilia-B patients individually
inhib_presence_A_percentage = number_of_inhibitors_present_hemo_A * 100 / number_of_hemo_A
inhib_presence_B_percentage = number_of_inhibitors_present_hemo_B * 100 / number_of_hemo_B
print(f"Percentage of inhibitor presence in Hemophilia-A: {inhib_presence_A_percentage}")
print(f"Percentage of inhibitor presence in Hemophilia-B: {inhib_presence_B_percentage}")

# Numbers and percentages of patients receiving prophylaxis for Hemophilia-A and Hemophilia-B individually
# find out if it's asking for total percentage or hemophilia's inself
percentage_of_patients_receiving_prophylaxis_A = number_of_patients_receiving_prophylaxis_A * 100 / number_of_hemo_A
percentage_of_patients_receiving_prophylaxis_B = number_of_patients_receiving_prophylaxis_B * 100 / number_of_hemo_B
print(f"Number of Hemophlia-A patients receiving prophylaxis: {number_of_patients_receiving_prophylaxis_A}, Percentage: {percentage_of_patients_receiving_prophylaxis_A}% ")

#  The percentage of patients receiving prophylaxis among hemophilia patients whose disease severity is moderate
percentage_of_moderate_patients_in_prophylaxis = number_of_prophylaxis_with_severity_moderate * 100 / (number_of_patients_receiving_prophylaxis_A + number_of_patients_receiving_prophylaxis_B)
print(f"Percentage of patients receiving prophylaxis with severity of moderate: {percentage_of_moderate_patients_in_prophylaxis}%")

#  Percentages of patients using plasma-derived and recombinant factor medications among
#  Hemophilia-A and Hemophilia-B patients receiving prophylaxis individual
























