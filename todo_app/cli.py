"""
Command-line interface module for the Todo App.

This module provides a menu-driven interface for managing todo tasks.
"""

from typing import Optional
from .tasks import TaskManager, Task


class TodoCLI:
    """
    Command-line interface for the Todo application.

    Provides a menu-driven interface for task management operations.
    """

    def __init__(self, task_manager: TaskManager) -> None:
        """
        Initialize the CLI with a task manager.

        Args:
            task_manager (TaskManager): The task manager instance to use
        """
        self.task_manager = task_manager

    def run(self) -> None:
        """
        Run the main application loop.

        Displays the menu and handles user choices until exit.
        """
        print("🎯 Welcome to Todo App!")
        print("Manage your tasks efficiently from the command line.\n")

        while True:
            self.show_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "6":
                print("\n👋 Thanks for using Todo App! Goodbye!")
                break
            elif choice in ["1", "2", "3", "4", "5"]:
                self.handle_choice(choice)
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

            print()  # Add spacing between operations

    def show_menu(self) -> None:
        """
        Display the main menu options.
        """
        print("\n" + "="*50)
        print("📋 TODO APP MENU")
        print("="*50)
        print("1. ➕ Add Task")
        print("2. 🗑️  Delete Task")
        print("3. ✏️  Update Task")
        print("4. 👀 View Tasks")
        print("5. ✅ Mark Task Complete")
        print("6. 🚪 Exit")
        print("="*50)

    def handle_choice(self, choice: str) -> None:
        """
        Handle the user's menu choice.

        Args:
            choice (str): The menu choice selected by the user
        """
        handlers = {
            "1": self.handle_add_task,
            "2": self.handle_delete_task,
            "3": self.handle_update_task,
            "4": self.handle_view_tasks,
            "5": self.handle_mark_complete
        }

        handler = handlers.get(choice)
        if handler:
            handler()

    def handle_add_task(self) -> None:
        """
        Handle adding a new task.
        """
        print("\n➕ ADD NEW TASK")
        print("-" * 20)

        # Get title
        while True:
            title = input("Enter task title (required): ").strip()
            if title:
                break
            print("❌ Title cannot be empty. Please try again.")

        # Get description
        description = input("Enter task description (optional): ").strip()

        try:
            task = self.task_manager.add_task(title, description)
            print(f"✅ Task added successfully! (ID: {task.id})")
        except ValueError as e:
            print(f"❌ Error adding task: {e}")

    def handle_delete_task(self) -> None:
        """
        Handle deleting a task.
        """
        print("\n🗑️  DELETE TASK")
        print("-" * 15)

        task_id = self._get_task_id("delete")
        if task_id is None:
            return

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ").strip().lower()
        if confirm not in ["y", "yes"]:
            print("❌ Deletion cancelled.")
            return

        if self.task_manager.delete_task(task_id):
            print(f"✅ Task {task_id} deleted successfully!")
        else:
            print(f"❌ Task {task_id} not found.")

    def handle_update_task(self) -> None:
        """
        Handle updating a task.
        """
        print("\n✏️  UPDATE TASK")
        print("-" * 15)

        task_id = self._get_task_id("update")
        if task_id is None:
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"❌ Task {task_id} not found.")
            return

        print(f"Current task: {task.title}")
        if task.description:
            print(f"Current description: {task.description}")

        # Get new title
        new_title = input("Enter new title (leave empty to keep current): ").strip()
        if not new_title:
            new_title = None

        # Get new description
        new_description = input("Enter new description (leave empty to keep current): ").strip()
        if not new_description:
            new_description = None

        try:
            if self.task_manager.update_task(task_id, new_title, new_description):
                print(f"✅ Task {task_id} updated successfully!")
            else:
                print(f"❌ Task {task_id} not found.")
        except ValueError as e:
            print(f"❌ Error updating task: {e}")

    def handle_view_tasks(self) -> None:
        """
        Handle viewing tasks with filtering options.
        """
        print("\n👀 VIEW TASKS")
        print("-" * 12)

        while True:
            print("\nFilter options:")
            print("1. All tasks")
            print("2. Pending tasks")
            print("3. Completed tasks")
            print("4. Back to main menu")

            filter_choice = input("Choose filter (1-4): ").strip()

            if filter_choice == "4":
                break
            elif filter_choice == "1":
                tasks = self.task_manager.get_all_tasks()
                filter_name = "All"
            elif filter_choice == "2":
                tasks = self.task_manager.get_tasks_by_status("pending")
                filter_name = "Pending"
            elif filter_choice == "3":
                tasks = self.task_manager.get_tasks_by_status("completed")
                filter_name = "Completed"
            else:
                print("❌ Invalid choice. Please enter 1-4.")
                continue

            self._display_tasks(tasks, filter_name)
            break

    def handle_mark_complete(self) -> None:
        """
        Handle marking a task as complete.
        """
        print("\n✅ MARK TASK COMPLETE")
        print("-" * 20)

        task_id = self._get_task_id("mark complete")
        if task_id is None:
            return

        if self.task_manager.mark_complete(task_id):
            print(f"✅ Task {task_id} marked as complete!")
        else:
            task = self.task_manager.get_task(task_id)
            if task:
                print(f"❌ Task {task_id} is already completed.")
            else:
                print(f"❌ Task {task_id} not found.")

    def _get_task_id(self, operation: str) -> Optional[int]:
        """
        Get a valid task ID from user input.

        Args:
            operation (str): Description of the operation for error messages

        Returns:
            int or None: The task ID if valid, None if cancelled
        """
        while True:
            task_id_str = input(f"Enter task ID to {operation} (or 'cancel'): ").strip()

            if task_id_str.lower() == "cancel":
                print("❌ Operation cancelled.")
                return None

            try:
                task_id = int(task_id_str)
                if task_id > 0:
                    return task_id
                else:
                    print("❌ Task ID must be a positive number.")
            except ValueError:
                print("❌ Invalid task ID. Please enter a number.")

    def _display_tasks(self, tasks: list[Task], filter_name: str) -> None:
        """
        Display a list of tasks.

        Args:
            tasks (List[Task]): Tasks to display
            filter_name (str): Name of the filter applied
        """
        if not tasks:
            print(f"\n📭 No {filter_name.lower()} tasks found.")
            return

        print(f"\n📋 {filter_name} Tasks ({len(tasks)} total):")
        print("-" * 60)

        for task in tasks:
            print(task)
            print("-" * 60)
