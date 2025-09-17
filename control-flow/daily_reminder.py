while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue  # Restart the loop

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message = f"Note: {message}. Consider completing it when you have free time."

    print("\nReminder:", message)
    break  # Exit after one successful reminder
