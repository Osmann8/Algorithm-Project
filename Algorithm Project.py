# Take personel information
ID = input("Enter your identification number: ")
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Take information about protein and it's level
deficient_protein = int(input("Enter the deficient factor protein's number: "))
while deficient_protein not in [8, 9]:
    deficient_protein = int(input("Enter the deficient factor protein's number: "))
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
    if deficient_protein == 8:
        print(f"3 times a week  to use the medication")
    else:
        print(f"2 times a week  to use the medication")
    




if severity == "moderate":
    number_of_bleeding = float(input("The number of bleeding in the past year: "))
    while number_of_bleeding < 0:
        number_of_bleeding = float(input("The number of bleeding in the past year: "))





