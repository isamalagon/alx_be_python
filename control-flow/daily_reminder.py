while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            priority_message = "a high priority task"
        case "medium":
            priority_message = "a medium priority task"
        case "low":
            priority_message = "a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue

    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    else:
        time_message = "that can be completed when you have free time."

    print(f"\nReminder: '{task}' is {priority_message} {time_message}")
    break
