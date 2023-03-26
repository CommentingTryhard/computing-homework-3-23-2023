passengercount = int(input("Enter numba of passenger: "))
distance = int(input("Enter distance of journey: "))

cost = distance*2+1
if passengercount >= 5:
  cost*=1.5
  
print(cost)
