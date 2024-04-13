# Program to generate Honest Harry Used Car Sales and Receipt
# Date written : Oct 10 ,2023-Oct 19,2023
# Autor:Shukrullah Zahiri



import datetime
#Define the current date and print it different format
CurDate = datetime.datetime.now() #Grab the current date from the system date.
formatted_date = CurDate.strftime("%B %d, %Y")
print(formatted_date)

# Define the constant
LICENSE_FEE_CHEAP_CAR = 75.00   # License fee for cheap cars (up to $5,000)
LICENSE_FEE_EXPENSIVE_CAR = 165.00  # License fee for expensive cars (over $5,000)
TRANSFER_FEE_RATE = 0.01  # Transfer fee rate (1%)
LUXURY_TAX_THRESHOLD = 20000.00 
LUXURY_TAX_RATE = 0.016  # Luxury tax rate (1.6%)
HST_RATE = 0.15  # Tax rate (15%)

#Function to calculate licence fee
def calculate_licence_fee(selling_price):
  return LICENSE_FEE_CHEAP_CAR if selling_price<=5000 else LICENSE_FEE_EXPENSIVE_CAR

# Input the customer details

CustFirstName = input("Enter the customer first name: ").title()
CustLastName = input("Enter the customer last name: ").title()

PhoneNum = input("Enter the phone number (10 digits): ")
PhoneNum = "("+PhoneNum[0:3]+")" + PhoneNum[3:6]+"-"+PhoneNum[6:]  

PlateNum = input("Enter plate number(XXX999): ").upper()
if PlateNum =="":
    print("write the plate number")
elif len(PlateNum)!=6:
    print("The lenght of plate number is not equal")
elif PlateNum[0:3].isalpha()==False:
    print("first three character must be alphabet")
elif PlateNum [3: ].isdigit()==False:
    print("Last three character must be digit")

CarMake = input("Enter the car make: ").title()

CarModel = input ("Enter the car model: ").capitalize()
Year =int(input("Enter the year: "))
SalesPrice = float(input("Selling price (Up to $50,000.00): "))
TradAmount= float(input("Trade in amount (Up to selling price): "))

# Function to calculate total sales price
Price_After_Trade = SalesPrice - TradAmount
LICENSE_FEE = calculate_licence_fee(SalesPrice)
Transfer_Fee = SalesPrice * TRANSFER_FEE_RATE

if SalesPrice > LUXURY_TAX_THRESHOLD:
        luxury_tax = SalesPrice * LUXURY_TAX_RATE
        Transfer_Fee += luxury_tax

SubTotal = Price_After_Trade + LICENSE_FEE + Transfer_Fee
hst = SubTotal * HST_RATE
total_sales_price = SubTotal + hst




# Calculate the number of years the customer will use to pay off the car
Years = int(input("Enter the number of years for payment: "))
FinancingFee = 39.99 * Years
TotalPrice = total_sales_price + FinancingFee
MonthlyPayment = TotalPrice / (Years * 12)

# Calculate the first payment date (30 days from the purchase date)
FirstPaymentDate = CurDate + datetime.timedelta(days=30)
formatted_first_payment_date = FirstPaymentDate.strftime("%b %d, %y")

# Create the receipt ID
CustomerInitials = CustFirstName[0] + CustLastName[0]
ReceiptID = f"{CustomerInitials}-{PlateNum[-3:]}-{PhoneNum[-4:]}"

# Display the receipt
print("\nHonest Harry Car Sales Invoice")
print(f"Invoice Date: {formatted_date}")
print(f"Used Car Sale and Receipt Receipt No: {ReceiptID}")
print(f"Sale Price: ${SalesPrice:.2f}")
print(f"Sold to: {CustFirstName} {CustLastName}")
print(f"Trade Allowance: ${TradAmount:.2f}")
print("----------------------------------")
print(f"Price after Trade: ${Price_After_Trade:.2f}")
print(f"License Fee: ${LICENSE_FEE:.2f}")
print(f"Transfer Fee: ${Transfer_Fee:.2f}")
print("----------------------------------")
print(f"Car Details: {Year} {CarMake} {CarModel}")
print(f"Subtotal: ${SubTotal:.2f}")
print(f"HST: ${hst:.2f}")
print("----------------------------------")
print(f"Total Sales Price: ${total_sales_price:.2f}")
print("------------------------------------------------------------")
print(f"Financing\tTotal\tMonthly")
print(f"# Years\t# Payments\tFee\tPrice\tPayment")
print(f"------------------------------------------------------------")
for i in range(1, Years + 1):
    print(f"{i}\t{Years * 12}\t${FinancingFee:.2f}\t${TotalPrice:.2f}\t${MonthlyPayment:.2f}")
print("------------------------------------------------------------")
print(f"Invoice Date: {formatted_date}\tFirst Payment Date: {formatted_first_payment_date}")
print("------------------------------------------------------------")
print("Best used cars at the best prices!")

# The program will continue until the user enters "END" for the Customer First Name.
while CustFirstName != "END":
    # Input the customer details for the next sale (if any)
    CustFirstName = input("\nEnter the customer first name (or 'END' to exit): ").title()
    if CustFirstName == "END":
        break  # Exit the loop if 'END' is entered
    CustLastName = input("Enter the customer last name: ").title()
    # ... (rest of the customer details input)
    # ... (rest of the calculations and receipt creation)