# Comment like a pro.

# Import required  libraries

# Set up  program constant.

# Set up program function.

from datetime import datetime

# Function to convert text to title case
def title_case(text):
    return ' '.join(word.capitalize() for word in text.split())

# Function to calculate the insurance premium
def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    basic_premium = 869.00
    discount_rate = 0.25
    extra_liability_cost = 130.00 * num_cars if extra_liability == 'Y' else 0
    glass_coverage_cost = 86.00 * num_cars if glass_coverage == 'Y' else 0
    loaner_car_cost = 58.00 * num_cars if loaner_car == 'Y' else 0

    total_extra_costs = extra_liability_cost + glass_coverage_cost + loaner_car_cost
    total_premium = basic_premium * (1 + (discount_rate * (num_cars - 1))) + total_extra_costs

    return total_premium

# Function to calculate total cost, HST, and monthly payment
def calculate_total_cost(total_premium, payment_option, down_payment=None):
    hst_rate = 0.15
    processing_fee = 39.99

    hst = total_premium * hst_rate
    total_cost = total_premium + hst

    if payment_option == 'Full':
        monthly_payment = total_cost / 8
    elif payment_option == 'Monthly':
        monthly_payment = (total_cost + processing_fee) / 8
    elif payment_option == 'Down Pay':
        total_cost -= down_payment
        monthly_payment = (total_cost + processing_fee) / 8
    else:
        raise ValueError("Invalid payment option")

    return total_cost, hst, monthly_payment

# Function to display the receipt
def display_receipt(customer_info, total_cost, hst, monthly_payment, claims):
    print("\n===== Receipt =====")
    print("Date:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("Customer Information:")
    for key, value in customer_info.items():
        print(f"{title_case(key)}: {value}")

    print("\nInsurance Information:")
    print(f"Total Premium: ${total_cost:.2f}")
    print(f"HST (15%): ${hst:.2f}")
    print(f"Total Cost: ${total_cost + hst:.2f}")
    print(f"Monthly Payment: ${monthly_payment:.2f}")

    print("\nPrevious Claims:")
    print("Claim #\tClaim Date\tAmount")
    print("---------------------------------")
    for i, (claim_date, claim_amount) in enumerate(claims, 1):
        print(f"{i}.\t{claim_date}\t${claim_amount:.2f}")

# Function to input and store previous claims
def input_previous_claims():
    claims = []
    while True:
        claim_date = input("Enter claim date (YYYY-MM-DD), press Enter to finish: ")
        if not claim_date:
            break
        claim_amount = float(input("Enter claim amount: $"))
        claims.append((claim_date, claim_amount))
    return claims

# Set up default values
next_policy_number = 1944
basic_premium = 869.00
discount_rate = 0.25
extra_liability_cost = 130.00
glass_coverage_cost = 86.00
loaner_car_cost = 58.00
hst_rate = 0.15
processing_fee = 39.99

# Main program loop
while True:
    customer_info = {}
    customer_info['first_name'] = input("Enter first name: ").title()
    customer_info['last_name'] = input("Enter last name: ").title()
    customer_info['address'] = input("Enter address: ")
    customer_info['city'] = input("Enter city: ").title()
    customer_info['province'] = input("Enter province (use valid options): ").upper()
    customer_info['postal_code'] = input("Enter postal code: ")
    customer_info['phone_number'] = input("Enter phone number: ")

    provinces = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE']
    while customer_info['province'] not in provinces:
        print("Invalid province. Please enter a valid province.")
        customer_info['province'] = input("Enter province (use valid options): ").upper()

    customer_info['num_cars'] = int(input("Enter the number of cars being insured: "))
    customer_info['extra_liability'] = input("Extra liability coverage (Y or N): ").upper()
    customer_info['glass_coverage'] = input("Glass coverage (Y or N): ").upper()
    customer_info['loaner_car'] = input("Loaner car coverage (Y or N): ").upper()

    payment_options = ['Full', 'Monthly', 'Down Pay']
    customer_info['payment_option'] = input("Payment option (Full, Monthly, or Down Pay): ").title()
    while customer_info['payment_option'] not in payment_options:
        print("Invalid payment option. Please enter a valid option.")
        customer_info['payment_option'] = input("Payment option (Full, Monthly, or Down Pay): ").title()

    if customer_info['payment_option'] == 'Down Pay':
        customer_info['down_payment'] = float(input("Enter the down payment amount: "))

    claims = input_previous_claims()

    total_premium = calculate_premium(
        customer_info['num_cars'],
        customer_info['extra_liability'],
        customer_info['glass_coverage'],
        customer_info['loaner_car']
    )

    total_cost, hst, monthly_payment = calculate_total_cost(
        total_premium,
        customer_info['payment_option'],
        customer_info.get('down_payment', 0)
    )

    display_receipt(customer_info, total_cost, hst, monthly_payment, claims)

    next_policy_number += 1
    proceed = input("Do you want to enter information for another customer? (Y/N): ").upper()
    if proceed != 'Y':
        break
