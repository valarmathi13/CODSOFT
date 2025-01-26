import json

def display_menu():
    print("\nTo-Do List Menu:")
    print("Add Task")
    print("Mark Done")
    print("Delete Task")
    print("View Tasks")
    print("Exit")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done:")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("please enter valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task to delete")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("please enter valid number.")

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("tasks saved.")

def load_tasks_from_file(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        print("tasks loaded.")
        return tasks
    except FileNotFoundError:
        print("No tasks found.")
        return []
    
def main():
    tasks = load_tasks_from_file("tasks.json")
    while True:
        display_menu()
        choice = input("Enter your choice:").lower()
        if choice == "add task":
            task = input("Enter task:")
            tasks.append({"task": task, "done": False})
            print("Task added.")
        elif choice == "delete task":
            delete_task(tasks)
        elif choice == "mark done":
            mark_done(tasks)
        elif choice == "view tasks":
            view_tasks(tasks)
        elif choice == "exit":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()


        