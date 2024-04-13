# Program to generate and calculate the automibles rents of Edsel Car Rental Company
# Date written : Sep 12,2023-Sep 19,2023
# Autor:Shukrullah Zahiri

# Define program constant
DAILY_RENTAL_COST = 55.00 #Daily rental rate in dollars
MILEAGE_RATE = 0.24 #Mileage rate in dollars per kilometer
INSURANCE_RATE = 14.00 #Insurance in dollar per day
DISCOUNT_RATE_RENTAL = 0.10 #Discount rate for rental cost(10%)
DISCOUNT_RATE_MILEAGE = 0.25 #Discount rate for mileage cost(25%)
HST_RATE = 0.15

CustName = input("Enter the customer name:  ")
PhonNum = input("Enter the phone number:  ")
NumDays = int(input("Enter number of days the car rented:  "))
OdoReaCarRent = int(input("Enter odometer reading when the car rented: "))
OdoReaCarRet =int(input("Enter odometer reading when the car was returned: "))

# Calculate total kilometers traveled
TotalKilos = OdoReaCarRet-OdoReaCarRent
#Calculate the rental cost
RentalCost = NumDays*55.00
#Calculate mileage cost
MileCost = TotalKilos*.24
#Calculate the insurance cost
InsCost = NumDays*14.00
#Calculate the total discount
TotDiscount = (RentalCost*.1)+(MileCost*.25)
#Calculate the total rental  cost
TotRentalCost = RentalCost + MileCost + InsCost - TotDiscount
#Calculate the HST
Hst = TotRentalCost*.15
#Calculate the final invoice
FinInvoice = TotRentalCost + Hst

print("Customer name: ", CustName)
print("Phone number: ", PhonNum)
print("Number of days: ",NumDays)
print("odometer reading when the car rented: ", OdoReaCarRent)
print("odometer reading when the car was returned: ",OdoReaCarRet)
print("Total kilometer traveled: ",TotalKilos)
print("Rental cost: ",RentalCost)
print("Mileage cost:",MileCost)
print("Insurance cost: ",InsCost)
print("Total discount: ",TotDiscount)
print("Total rental cost: ",TotRentalCost)
print("Hst: ",Hst)
print("Final invoice: ",FinInvoice)
