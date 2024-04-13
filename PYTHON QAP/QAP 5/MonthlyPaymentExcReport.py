#Comment like a pro.
# Import any required libraries
import datetime

Today = datetime.datetime.now()
TodayDSP = datetime.datetime.strftime(Today, "%d-%b-%y")

# Defaults from OSICDef.dat
next_policy_number = 2032
BASIC_RATE = 869.00
DISCOUNT_PERCENTAGE = 0.25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_OPTION_COST = 58.00
HST_RATE = 0.15
PROCESS_FEES = 39.99

# Function to calculate monthly payment and generate exceptional report
def calculate_monthly_payment():
    # Print main heading and column headings
    print("ONE STOP INSURANCE COMPANY                                                         ")
    print(f"MONTHLY PAYMENT LISTING AS OF {TodayDSP:<10s}                                     ") 
    print()
    print("POLICY CUSTOMER              TOTAL                  TOTAL       DOWN       MONTHLY ")
    print("NUMBER NAME                  PREMIUM      HST       COST       PAYMENT     PAYMENT ")
    print("===================================================================================")

    # Initialize counters and accumulators for summary/analytic
    total_policies = 0
    total_premium = 0.0
    total_hst = 0.0
    total_cost = 0.0
    total_monthly_payment = 0.0

    # Open the file with the "r" mode for read
    with open("Policies.dat", "r") as policies_file:
        # Set up the loop to process all the records in the file
        for CustRecord in policies_file:
            # Input - read the record and split into a list
            CustLst = CustRecord.strip().split(",")

            # Assign variables to each item in the list that are required in the report
            policy_number = CustLst[0].strip()
            customer_name = CustLst[2].strip()
            policy_date = CustLst[1].strip()
            payment_option = CustLst[13].strip().upper()
            down_payment = float(CustLst[14].strip())

            # Skip policies with payment option Full
            if payment_option == 'FULL':
                continue

            # Convert relevant values to appropriate types
            policy_number = int(policy_number)
            insurance_premium = float(CustLst[9].strip())

            # Calculate total premium
            total_premium = insurance_premium

            # Calculate HST
            total_hst = total_premium * HST_RATE

            # Calculate total cost
            total_cost = total_premium + total_hst

            # Calculate monthly payment
            monthly_payment = (total_cost - down_payment + PROCESS_FEES) / 12

            # Print exceptional report line
            print(f"{policy_number: <6} {customer_name: <20s} "
                  f"${total_premium:<6,.2f}     ${total_hst:,.2f}      ${total_cost:,.2f}       "
                  f"${down_payment:,.2f}       ${monthly_payment:<5,.2f}")

            # Update counters and accumulators
            total_policies += 1
            total_monthly_payment += monthly_payment

    print("====================================================================================")       
    # Print total policies summary
    print(f"Total policies:             {total_policies: <3}        "
          f"${total_premium:<11,.2f} ${total_hst:,.2f}      ${total_cost:,.2f}        "
          f"${total_monthly_payment:,.2f}")

calculate_monthly_payment()
