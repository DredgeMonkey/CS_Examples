flat_charge = 20
premium_ground_charge = 125.00
def ground_shipping_cost(weight):
  if weight <= 2:
    return weight * 1.50 + flat_charge
  elif weight >= 2 and weight <= 6:
    return weight * 3.00 + flat_charge
  elif weight >= 6 and weight <= 10:
    return weight * 4.00 + flat_charge
  else:
    return weight * 4.75 + flat_charge 
    
print(ground_shipping_cost(8.4))

def drone_shipping_cost(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight >= 2 and weight <= 6:
    return weight * 3.00
  elif weight >= 6 and weight <= 10:
    return weight * 12.00
  else:
    return weight * 14.25
  
print(drone_shipping_cost(1.5))


def print_cheapest_shipping_method(weight):
  
  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)
  premium = premium_ground_charge
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost= ground
  elif premium < ground and premium < drone:
    method = "Premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
    
  print(
    "The cheapest shipping available is $%.2f with %s shipping"
  % (cost, method)
  )
  
print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.8)
  
 
