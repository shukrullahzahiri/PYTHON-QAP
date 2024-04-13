# Program to generate St.John's Marina & Yacht Club Yearly Member Receipt
# Date written : Sep 19,2023-Oct 06,2023
# Autor:Shukrullah Zahiri

 
# Define program constant
EVEN_SITE_PRICE = 80.00
ODD_SITE_PRICE = 120.00
ALTERNATE_MEMBER_PRICE = 5.00
WEEKLY_CLEANING_PRICE = 50.00
VIDEO_SURVEILLANCE_PRICE = 35.00
SALES_TAX_RATE = 0.15
STANDARD_MEMBER_DUES = 75.00
EXECUTIVE_MEMBER_DUES = 150.00
PROCESSING_FEE = 59.99
CANCELLATION_FEE_RATE = 0.6

#Gather user input
SiteNum = int(input("Enter site number(1-100): "))
MemName = input("Enter the member name: ")
StAdd = input("Enter the member street address: ")
City = input("Enter the city; ")
Prov = input(" Enter the province: ")
PostCode = input("Enter the postal code: ")
PhoneNum = input("Enter the phone number(###-###-####)")
CellNum = input("Enter the cell number: ")
MemType = input("Enter the member type( S for standard, E for executive): ")
AltMem = int(input("Enter number of alternate member: "))
WeekSitClean = input("Enter the weekly site cleaning: Y for yes, N for No")
VidSurv = input("Enter the video surveilliance: Y for yes, N for No")



# Generate result with requied calculation.

def calculate_site_charge(site_number):
    if site_number % 2 == 0:
        return 80.00  # Even numbered sites cost $80.00 per month
    else:
        return 120.00  # Odd numbered sites cost $120.00 per month

    #Calculate the cost of alternative members
ALTERNATE_MEMBER_COST =AltMem * ALTERNATE_MEMBER_PRICE


# Calculate extra charges
def calculate_extra_charges(weekly_cleaning, video_surveillance):
    extra_charges = 0
    if weekly_cleaning == 'Y':
        extra_charges += WEEKLY_CLEANING_PRICE
    if video_surveillance == 'Y':
        extra_charges += VIDEO_SURVEILLANCE_PRICE
    return extra_charges

# Function to calculate total monthly charges
def calculate_total_monthly_fees(site_number, membership_type, alternate_members, weekly_cleaning, video_surveillance):
    site_charges = calculate_site_charge( site_number)
    extra_charges = calculate_extra_charges(weekly_cleaning, video_surveillance)
    alternate_member_charges = alternate_members * ALTERNATE_MEMBER_PRICE
    subtotal = site_charges + extra_charges + alternate_member_charges
    sales_tax = subtotal * SALES_TAX_RATE
    monthly_dues = STANDARD_MEMBER_DUES if membership_type == 'S' else EXECUTIVE_MEMBER_DUES
    total_monthly_charges = subtotal + sales_tax + monthly_dues
    return site_charges, extra_charges, alternate_member_charges, subtotal, sales_tax, total_monthly_charges, monthly_dues

# Function to calculate total yearly fees
def calculate_total_yearly_fees(total_monthly_fees):
    return total_monthly_fees * 12

# Function to calculate monthly payment
def calculate_monthly_payment(total_yearly_fees):
    return (total_yearly_fees + PROCESSING_FEE) / 12

# Function to calculate cancellation fee
def calculate_cancellation_fee(total_yearly_fees):
    return total_yearly_fees * CANCELLATION_FEE_RATE

# Function to display receipt
def display_receipt(site_number, member_name, street_address, city, province, postal_code, phone_number, cell_number, membership_type, alternate_members, weekly_cleaning, video_surveillance):
    site_charges, extra_charges, alternate_member_charges, subtotal, sales_tax, total_monthly_charges, monthly_dues = calculate_total_monthly_fees(site_number, membership_type, alternate_members, weekly_cleaning, video_surveillance)
    total_yearly_fees = calculate_total_yearly_fees(total_monthly_charges)
    monthly_payment = calculate_monthly_payment(total_yearly_fees)
    cancellation_fee = calculate_cancellation_fee(total_yearly_fees)

    # Display the receipt
    print("St. John’s Marina & Yacht Club")
    print("Yearly Member Receipt")
    print("Client Name and Address:")
    print(MemName)
    print(StAdd)
    print(f"{city}, {province} {postal_code}")
    print(f"Phone: {phone_number} (H)")
    print(f"{cell_number} (C)")
    print(f"Site #: {SiteNum} Member type: {'Standard' if membership_type == 'S' else 'Executive'}")
    print(f"Alternate members: {alternate_members}")
    print(f"Weekly site cleaning: {'Yes' if weekly_cleaning == 'Y' else 'No'}")
    print(f"Video surveillance: {'Yes' if video_surveillance == 'Y' else 'No'}")
    print(f"Site charges: ${site_charges:.2f}")
    print(f"Extra charges: ${extra_charges:.2f}")
    print(f"Alternate member charges: ${alternate_member_charges:.2f}")
    print("-------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales tax (HST): ${sales_tax:.2f}")
    print("-------------")
    print(f"Total monthly charges: ${total_monthly_charges:.2f}")
    print(f"Monthly dues: ${monthly_dues:.2f}")
    print("-------------")
    print(f"Total monthly fees: ${total_monthly_fees:.2f}")
    print(f"Total yearly fees: ${total_yearly_fees:.2f}")
    print(f"Monthly payment: ${monthly_payment:.2f}")
    print(f"Issued: YYYY-MM-DD")
    print("HST Reg No: 549-33-5849-4720-9885")
    print(f"Cancellation fee: ${cancellation_fee:.2f}")
