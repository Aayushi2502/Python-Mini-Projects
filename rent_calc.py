#program to calculate rent per head for roommates to split expenses made monthly
#inputs include rent of apartment, electricity spent,total amt spent on food,number of people in flat
#output shows amt each member has to pay

rent=int(input("Rent of the apartment: "))
food=int(input("Money spent on food: "))
elec=int(input("Units of electricity used: "))
unit=int(input("Charge per unit of electricity: "))
members=int(input("Number of roommates: "))

elec_bill=elec*unit
total_spend= rent+food+ elec_bill

total_rent=total_spend//members
print(total_rent)