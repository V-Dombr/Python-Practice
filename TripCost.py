# It doesn't work

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

city = raw_input("Enter city:")
days = int(raw_input("How many days:"))
spending_money = float(raw_input("Enter your spendings:"))

# print city
# print days
# print spending_money

print trip_cost(city, days, spending_money)


"""def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)"""