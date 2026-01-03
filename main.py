#!/usr/bin/env python3
"""
Todo App - Main Entry Point

A simple command-line todo application for managing tasks.
"""

from todo_app.tasks import TaskManager
from todo_app.cli import TodoCLI


def main() -> None:
    """
    Main entry point for the Todo application.

    Initializes the task manager and CLI, then starts the application.
    """
    try:
        # Initialize components
        task_manager = TaskManager()
        cli = TodoCLI(task_manager)

        # Run the application
        cli.run()

    except KeyboardInterrupt:
        print("\n\n⚠️  Application interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("Please report this issue if it persists.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
