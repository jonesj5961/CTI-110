# In-class formatting examples

rent =5000
phone =125.45255445
internet =56.444
electric =588.04
gas ="Not Applicable"
total =rent + phone + internet + electric

print(f"{'BILL,:<20'}{'AMOUNT'}")
print("-+*" * 18)
print(f"{'Rent:':<20}${rent:,.2f}")
print(f"{'Phone:':<20}${phone:,.2f}")
print(f"{'Internet:':<20}${internet:,.2f}")
print(f"{'Electric:':<20}${electric:,.2f}")
print(f"{'Gas:':<20}{gas}")
print("---" * 18)
print(f"{'Total:':<20}${total:,.2f}")
