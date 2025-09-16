print("Calculate fuel consumtion.")
feed = input("Enter travel distance(kilometers): ")
distance = (int(feed))
feed = input("Enter fuel usage(liters): ")
fuelusage = (int(feed))
consumption = (fuelusage/distance)*100
consumption = int(consumption)
print(f"Fuel consumption is {consumption} l per 100 km")