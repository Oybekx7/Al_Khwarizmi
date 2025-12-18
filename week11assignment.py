def book_session(members_db, schedule_db, member_id, class_name, spots):
    #Member Check:
    if member_id not in members_db:
        raise KeyError("Member ID not found")
    
    #Class Check:
    if class_name not in schedule_db:
        raise KeyError("Class not found")
    
    #Input Validation:
    if type(spots) is not int or spots < 1:
        raise ValueError("Spots must be positive integer")
    
    #Cost Calculation:
    cost_per_spot = schedule_db[class_name]["cost"]
    total_cost = spots * cost_per_spot
    
    if members_db[member_id]["pass_type"] == "Premium":
        total_cost = 0
        
    #Credit Check:
    if members_db[member_id]["credits"] < total_cost:
        raise ValueError("Insufficient credits")
    
    #Action:
    members_db[member_id]["credits"] -= total_cost
    
    #Return:
    return total_cost

def process_gym_bookings(members_db, schedule_db, booking_queue):

    results = {'credits_used': 0, 'declined_bookings': 0}
    for member_id, class_name, spots in booking_queue:
        try:
            cost = book_session(members_db, schedule_db, member_id, class_name, spots)
            results['credits_used'] += cost
            
        except (KeyError, ValueError) as e:
            print(f"Booking Error for {member_id}: {e}")
            results['declined_bookings'] += 1
                    
    return results

schedule = {
    "Yoga":   {"cost": 5},
    "Boxing": {"cost": 10}
}

members = {
    "M1": {"credits": 20, "pass_type": "Standard"},
    "M2": {"credits": 5,  "pass_type": "Premium"} # Free classes
}

queue = [
    ("M1", "Yoga", 2),      # Valid. Cost: 10. Rem: 10.
    ("M2", "Boxing", 10),   # Valid. Cost: 0 (Premium). Rem: 5.
    ("M1", "Boxing", 2),    # Error: Cost 20 > 10.
    ("M9", "Zumba", 1),     # Error: Member ID not found.
    ("M1", "Pilates", 1),   # Error: Class not found.
    ("M2", "Yoga", 0)       # Error: Spots must be positive integer.
]

final = process_gym_bookings(members, schedule, queue)
print(final)