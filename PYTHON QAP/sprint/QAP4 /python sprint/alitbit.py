import datetime

# Function to calculate maintenance schedule dates
def calculate_maintenance_schedule(purchase_date):
    basic_cleaning_date = purchase_date + datetime.timedelta(days=10)
    tube_fluid_check_date = purchase_date + datetime.timedelta(weeks=3)
    major_inspection_date = purchase_date + datetime.timedelta(days=180)

    return basic_cleaning_date, tube_fluid_check_date, major_inspection_date

# Function to calculate monthly amortization
def calculate_amortization(cost):
    useful_life_months = 180  # 15 years
    salvage_value = 0.10 * cost
    monthly_amortization = (cost - salvage_value) / useful_life_months

    return monthly_amortization

# Input from the user
purchase_cost = float(input("Enter the cost of the equipment: $"))
purchase_date_str = input("Enter the purchase date (YYYY-MM-DD): ")
purchase_date = datetime.datetime.strptime(purchase_date_str, "%Y-%m-%d").date()

# Calculate maintenance schedule dates
basic_cleaning_date, tube_fluid_check_date, major_inspection_date = calculate_maintenance_schedule(purchase_date)

# Calculate monthly amortization
monthly_amortization = calculate_amortization(purchase_cost)

# Display maintenance schedule and amortization details
print("Maintenance Schedule:")
print(f"Basic Cleaning (10 days): {basic_cleaning_date}")
print(f"Tube and Fluid Checks (3 weeks): {tube_fluid_check_date}")
print(f"Major Inspection (6 months): {major_inspection_date}")
print("\nAmortization Details:")
print(f"Monthly Amortization: ${monthly_amortization:.2f}")
