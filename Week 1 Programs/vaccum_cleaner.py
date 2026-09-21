def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

environment = {"A": "Dirty", "B": "Dirty"}
current_location = "A"

for step in range(4):
    status = environment[current_location]
    action = reflex_vacuum_agent(current_location, status)
    
    print(f"Step {step + 1}: Vacuum is in Room {current_location} ({status}) -> Action: {action}")
    
    if action == "Suck":
        environment[current_location] = "Clean"
    elif action == "Right":
        current_location = "B"
    elif action == "Left":
        current_location = "A"