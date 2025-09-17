while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue

    if time_bound == "yes":
        final_message = f"{base_message} that requires immediate attention today!"
    else:
        final_message = f"{base_message}. Consider completing it when you have free time."

    print("\nReminder:", final_message)
    break
