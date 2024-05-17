import json
import os

class Task:
    def __init__(self, description, priority, due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date = f"Due Date: {self.due_date}" if self.due_date else "No Due Date"
        return f"Description: {self.description}\nPriority: {self.priority}\nStatus: {status}\n{due_date}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}:")
                print(task)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task(task['description'], task['priority'], task['due_date'], task['completed']) for task in data]

def main():
    todo_list = ToDoList()
    filename = "tasks.json"
    todo_list.load_from_file(filename)

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (YYYY-MM-DD) (Press Enter for no due date): ")
            if due_date:
                due_date = due_date.strip()
            else:
                due_date = None
            todo_list.add_task(Task(description, priority, due_date))
            print("Task added successfully.")
            todo_list.save_to_file(filename)
        elif choice == "2":
            task_index = int(input("Enter index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)
            todo_list.save_to_file(filename)
        elif choice == "3":
            task_index = int(input("Enter index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
            todo_list.save_to_file(filename)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
