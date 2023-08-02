# To-Do List App in Python

def print_menu():
    print("----------- To-Do List ------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("---------- Tasks ----------")
        for i, task in enumerate(todo_list):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i + 1}. {task['task']} - {status}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(todo_list):
        todo_list[task_num]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def edit_task(todo_list):
    view_tasks(todo_list)
    task_num = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_num < len(todo_list):
        new_task = input("Enter the new task: ")
        todo_list[task_num]["task"] = new_task
        print("Task edited successfully!")
    else:
        print("Invalid task number.")

def delete_task(todo_list):
    view_tasks(todo_list)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(todo_list):
        del todo_list[task_num]
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    todo_list = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            edit_task(todo_list)
        elif choice == '5':
            delete_task(todo_list)
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()

