#Comment like a pro.
# Import any required libraries

import datetime
Today = datetime.datetime.now()
TodayDSP = datetime.datetime.strftime(Today, "%d-%m-%Y")

# Define any program constants
BASIC_RATE = 869.00
DISCOUNT_PERCENTAGE = 25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_OPTION_COST = 58.00

# Function to calculate insurance premium and extra costs
def calculate_premium_and_costs():
    # Print main heading and column headings
    print("ONE STOP INSURANCE COMPANY                                                        ")
    print(f"POLICY LISTING AS OF {TodayDSP:<10s}                                             ") 
    print()
    print("POLICY CUSTOMER              POLICY        INSURANCE         EXTRA          TOTAL ")
    print("NUMBER NAME                   DATE          PREMIUM          COSTS         PREMIUM")
    print("==================================================================================")

# Initialize counters and accumulators for summary/analytic
total_policies = 0
total_premium = 0.0
total_hst = 0.0
total_insurance_premium = 0.0
    # Open the file with the "r" mode for read
f= open("Policies.dat", "r")
        # Set up the loop to process all the records in the file
for CustRecord in f:
            # Input - read the record and split into a list
            CustLst = CustRecord.split(",")

            # Assign variables to each item in the list that are required in the report
            # The .strip() method removes any spaces in the front or back of a value
            policy_number = CustLst[0].strip()
            customer_name = CustLst[2].strip()
            policy_date = CustLst[1].strip()
            insurance_premium = float(CustLst[9].strip())
            extra_liability = CustLst[10].strip().upper() == 'Y'
            glass_coverage = CustLst[11].strip().upper() == 'Y'
            loaner_car_option = CustLst[12].strip().upper() == 'Y'

            # Convert relevant values to appropriate types
            policy_number = int(policy_number)
            num_cars = int(CustLst[9].strip())

            # Calculate insurance premium for the first automobile
            discount_rate = DISCOUNT_PERCENTAGE / 100 if num_cars > 1 else 0.0
            insurance_premium = BASIC_RATE * (1 - discount_rate) * num_cars

            # Calculate extra costs
            total_extra= 0
            if extra_liability:
                total_extra += EXTRA_LIABILITY_COST * (num_cars - 1)
            if glass_coverage:
                total_extra += GLASS_COVERAGE_COST * num_cars
            if loaner_car_option:
                total_extra += LOANER_CAR_OPTION_COST * num_cars

            # Calculate total premium with costs
            total_premium = insurance_premium + total_extra

            # Print detailed report line
            print(f"{policy_number: <6} {customer_name: <24s} {policy_date: <10} "
                  f"${insurance_premium:,.2f} ${total_extra:,.2f} ${total_premium:,.2f}")
            # Update counters and accumulators
            total_policies += 1
            total_insurance_premium += insurance_premium
            total_extra += total_extra

print("======================================================================")       
# Print total policies summary
print(f"total policies: {total_policies: <3} "                  f"${total_insurance_premium:,.2f} ${total_extra:,.2f} ${total_insurance_premium + total_extra:,.2f}")

