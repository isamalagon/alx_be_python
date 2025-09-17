while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            urgency = "requires immediate attention today!" if time_bound == "yes" else "should be prioritized soon."
        case "medium":
            urgency = "is important but flexible." if time_bound == "yes" else "can be scheduled when convenient."
        case "low":
            urgency = "is low priority but time-sensitive—don't forget!" if time_bound == "yes" else "can be done when you have free time."
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue

    print(f"\nReminder: '{task}' is a {priority} priority task that {urgency}")
    break
