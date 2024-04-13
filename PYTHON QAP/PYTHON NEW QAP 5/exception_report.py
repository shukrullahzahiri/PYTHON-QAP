# Function to generate exceptional report
import datetime

Today = datetime.datetime.now()
TodayDSP = datetime.datetime.strftime(Today, "%d-%b-%y")

# Define any program constants
BASIC_RATE = 869.00
DISCOUNT_PERCENTAGE = 25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_OPTION_COST = 58.00
HST_RATE = 0.15
PROCESS_FEES = 39.99

# Initialize counters and accumulators for summary/analytic
total_policies = 0
total_insurance_premium = 0.0
total_extra = 0.0

# Function to calculate insurance premium and extra costs
def generate_exceptional_report():
    # Print main heading and column headings
    print("ONE STOP INSURANCE COMPANY                                                   ")
    print(f"MONTHLY PAYMENT LISTING AS OF {TodayDSP}                                    ") 
    print()
    print("POLICY CUSTOMER              POLICY                TOTAL     DOWN     MONTHLY")
    print("NUMBER NAME                   DATE       HST       COST     PAYMENT   PAYMENT")
    print("=============================================================================")

    # Open the file with the "r" mode for read
    with open("Policies.dat", "r") as policies_file:
        # Set up the loop to process all the records in the file
        for CustRecord in policies_file:
            # Input - read the record and split into a list
            CustLst = CustRecord.strip().split(",")

            # Assign variables to each item in the list that are required in the report
            policy_number = CustLst[0].strip()
            customer_name = f"{CustLst[2].strip()} {CustLst[3].strip()}"
            policy_date = CustLst[1].strip()
            total_premium = float(CustLst[9].strip())
            down_payment = float(CustLst[-1].strip())

            # Check if payment is Monthly or Down Pay
            is_monthly_payment = CustLst[12].strip().upper() == 'MONTHLY'
            is_down_payment = CustLst[12].strip().upper() == 'DOWN PAY'

            # Calculate HST
            hst = total_premium * HST_RATE

            # Calculate total cost
            total_cost = total_premium + hst

            # Subtract down payment from total cost if it is a Down Pay
            if is_down_payment:
                total_cost -= down_payment

            # Calculate monthly payment
            monthly_payment = (total_cost + PROCESS_FEES) / 12

            # Print detailed report line for exceptions
            if is_monthly_payment or is_down_payment:
                print(f"{policy_number: <6} {customer_name: <24} {policy_date: <10} "
                      f"${total_premium:,.2f} ${hst:,.2f} ${total_cost:,.2f} "
                      f"${down_payment:,.2f} ${monthly_payment:,.2f}")

                # Update counters and accumulators
                total_policies += 1
                total_insurance_premium += total_premium
                total_extra += total_cost - total_premium

    print("======================================================================")       
    print(f"total policies: {total_policies: <3} "
          f"${total_insurance_premium:,.2f} ${total_extra:,.2f} "
          f"${total_insurance_premium + total_extra:,.2f}")

# Run the function to generate exception report
generate_exceptional_report()
