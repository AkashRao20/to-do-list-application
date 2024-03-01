def welcome_message():
    """Prints a welcome message to the user."""
    print("""
                Welcome to your To-Do List Application!

    How can I help you today?

    1. Display To-Do List
    2. Add a Task
    3. Mark a Task as Completed
    4. Remove a Task
    5. Quit

    Please enter the number corresponding to your desired action:
    """)

def display_todo_list(todo_list):
    """Displays the current to-do list with task numbers and completion status."""
    if not todo_list:
        print("\nYour to-do list is currently empty.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list):
        completion_status = "Done" if task[1] else "Pending"
        print(f"  {i+1}. {task[0]} ({completion_status})")

def add_task(todo_list):
    """Prompts the user to add a new task and appends it to the list."""
    new_task = input("\nEnter the name of the new task: ")
    todo_list.append([new_task, False])  # Append new task with "False" for pending status
    print(f"\nTask '{new_task}' added to your to-do list.")

def mark_task_completed(todo_list):
    """Marks a task as completed based on user input."""
    if not todo_list:
        print("\nYour to-do list is currently empty.")
        return

    display_todo_list(todo_list)  # Display list for reference
    try:
        task_number = int(input("\nEnter the number of the task you want to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1][1] = True  # Mark task as completed
            print(f"\nTask '{todo_list[task_number - 1][0]}' marked as completed.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

def remove_task(todo_list):
    """Removes a task from the list based on user input."""
    if not todo_list:
        print("\nYour to-do list is currently empty.")
        return

    display_todo_list(todo_list)  # Display list for reference
    try:
        task_number = int(input("\nEnter the number of the task you want to remove: "))
        if 1 <= task_number <= len(todo_list):
            del todo_list[task_number - 1]  # Remove task
            print(f"\nTask removed.")  # No need to access removed task's index
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

def main():
    """Manages the main application loop and user interactions."""
    todo_list = []  # Initialize empty to-do list
    welcome_message()

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            continue

        if choice == 1:
            display_todo_list(todo_list)
        elif choice == 2:
            add_task(todo_list)
        elif choice == 3:
            mark_task_completed(todo_list)
        elif choice == 4:
            remove_task(todo_list)
        elif choice == 5:
            print("\nGoodbye! See you next time.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
