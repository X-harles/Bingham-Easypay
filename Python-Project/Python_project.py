print("________Bingham EasyPay_______")
print("_____________'BEP'_____________")
print("_____""EasyAccess EasyPay""_____")
name = input("Input your name here: ")
print("________Welcome " + name + "________")

print("____________________________________________________________")

print("Kindly make your payments from the available bills")

print("____________________________________________________________")
# bill = 0

l1 = "laundry_services"
l2 = "accommodation_fees"
l3 = "provisions"
l4 = "tuition_fees"
l5 = "maintenance_fees"
l6 = "games"
l7 = "development_levy"
l8 = "library_services"
l9 = "registration_charges"
l10 = "ict_services"
l11 = "entrepreneur_fees"
l12 = "examination_fees"
l13 = "health_insurance "
l14 = "faculty_payments"
l15 = "src_payments"


print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"l3: {l3}")
print(f"l4: {l4}")
print(f"l5: {l5}")
print(f"l6: {l6}")
print(f"l7: {l7}")
print(f"l8: {l8}")
print(f"l9: {l9}")
print(f"l10: {l10}")
print(f"l11: {l11}")
print(f"l12: {l12}")
print(f"l13: {l13}")
print(f"l14: {l14}")
print(f"l15: {l15}")

print("____________________________________________________________")

print("Kindly place a payment from the following bills: ")

print("____________________________________________________________")

print("Laundry_Services = ₦7,500")
print("Accommodation_Fees = ₦85,000")
print("Provisions = ₦30,000")
print("Tuition_Fees = ₦650,000")
print("Maintenance_Fees = ₦55,000")
print("Games = ₦15,000")
print("Development_Levy = ₦101,000")
print("Library_Services = ₦30,500")
print("Registration_Charges = ₦20,500")
print("ICT_Services = ₦60,000")
print("Entrepreneur_Fees = ₦20,000")
print("Examination_Fees = ₦40,000")
print("Health_Insurance = ₦20,000")
print("Faculty_Payments = ₦12,000")
print("SRC_Payments = ₦5,000")

laundry_services = 7500
accommodation_fees = 85000
provisions = 30000
tuition_fees = 650000
maintenance_fees = 55000
games = 15000
development_levy = 101000
library_services = 30500
registration_charges = 20500
ict_services = 60000
entrepreneur_fees = 20000
examination_fees = 40000
health_insurance = 20000
faculty_payments = 12000
src_payments = 5000


print("____________________________________________________________")

purchase = input("Kindly input payment: ").lower()

print("____________________________________________________________")

if purchase == l1:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = laundry_services * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
    the vat price is_N{vat}
    total price is___N{price}

 "Thank You Using Bingham EasyPay"
    """)
elif purchase == l2:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = accommodation_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
    the vat price is_N{vat}
    total price is___N{price}

    "Thank You Using Bingham EasyPay"
    """)
elif purchase == l3:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = provisions * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l4:
    amount = int(input("Input the amount of person's you wish to pay for: "))#
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = tuition_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

    "Thank You Using Bingham EasyPay"
    """)
elif purchase == l5:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = maintenance_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l6:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = games * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l7:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = development_levy * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

    "Thank You Using Bingham EasyPay"
    """)
elif purchase == l8:
    amount = int(input("Input the amount of person's you wish to pay for: "))
   print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = library_services * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

    "Thank You Using Bingham EasyPay"
    """)
elif purchase == l9:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = registration_charges * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)

elif purchase == l10:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = ict_services * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l11:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = entrepreneur_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l12:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = examination_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)
elif purchase == l13:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = examination_fees * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

    "Thank You Using Bingham EasyPay"
    """)
elif purchase == l14:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = health_insurance * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}

     "Thank You Using Bingham EasyPay"
    """)

elif purchase == l15:
    amount = int(input("Input the amount of person's you wish to pay for: "))
    print("____________________________________________________________")
    Matric_Number = input("Input Matriculation Number: ")
    total = src_payments * amount
    vat = (total * 0.075) / 100
    price = total + vat
    print(f"""
        the vat price is_N{vat}
        total price is___N{price}
    "Thank You Using Bingham EasyPay"
    """)
