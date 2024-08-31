def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if "Dhaka" == city:
        return 183
    
    elif "Comilla" == city:
        return 220
    
    elif "Cox" == city:
        return 222
    
    elif "Chittagong" == city:
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    
    elif days >= 3:
        return 40 * days - 20
    
    else:
        return 40 * days
    
def total_cost(day,city):
    return (hotel_cost(day) + plane_ride_cost(city) + rental_car_cost(day))

numDay = int(input("Enter the Number of Days you Are Going to Stay: "))
cityy = input("Enter the City [Dhaka, Comilla, Cox, Chittagong: ]")

total = total_cost(numDay, cityy)

print(f"Hotel Cost : {hotel_cost(numDay)}")
print(f"Plane Ride Cost: {plane_ride_cost(cityy)}")
print(f"Rental Car Cost: {rental_car_cost(numDay)}")
print(f"Total Cost : {total}")