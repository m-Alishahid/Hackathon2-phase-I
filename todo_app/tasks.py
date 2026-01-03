"""
Task management module for the Todo App.

This module contains the Task model and TaskManager class for managing
todo tasks in memory.
"""

from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single todo task.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Task title (required)
        description (str): Task description (optional)
        status (str): Task status ("pending" or "completed")
        created_at (datetime): Task creation timestamp
        completed_at (datetime): Task completion timestamp (None if not completed)
    """

    def __init__(self, title: str, description: str = "") -> None:
        """
        Initialize a new task.

        Args:
            title (str): Task title (required, max 100 characters)
            description (str): Task description (optional, max 500 characters)

        Raises:
            ValueError: If title is empty or too long
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        if len(title) > 100:
            raise ValueError("Task title cannot exceed 100 characters")
        if len(description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")

        self.id: Optional[int] = None  # Set by TaskManager
        self.title: str = title.strip()
        self.description: str = description.strip()
        self.status: str = "pending"
        self.created_at: datetime = datetime.now()
        self.completed_at: Optional[datetime] = None

    def mark_complete(self) -> None:
        """
        Mark the task as completed.

        Sets status to "completed" and records completion timestamp.
        Does nothing if already completed.
        """
        if self.status == "pending":
            self.status = "completed"
            self.completed_at = datetime.now()

    def __str__(self) -> str:
        """
        Return a formatted string representation of the task.

        Returns:
            str: Formatted task information
        """
        status_icon = "✓" if self.status == "completed" else "○"
        completed_info = f" (Completed: {self.completed_at.strftime('%Y-%m-%d %H:%M')})" if self.completed_at else ""
        desc_info = f"\n  Description: {self.description}" if self.description else ""

        return f"{status_icon} [{self.id}] {self.title}{desc_info}\n  Created: {self.created_at.strftime('%Y-%m-%d %H:%M')}{completed_info}"


class TaskManager:
    """
    Manages a collection of tasks in memory.

    Provides CRUD operations and status management for tasks.
    """

    def __init__(self) -> None:
        """Initialize an empty task manager."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the manager.

        Args:
            title (str): Task title
            description (str): Task description (optional)

        Returns:
            Task: The newly created task
        """
        task = Task(title, description)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List[Task]: Copy of all tasks
        """
        return self.tasks.copy()

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """
        Get tasks filtered by status.

        Args:
            status (str): Status to filter by ("pending" or "completed")

        Returns:
            List[Task]: Tasks with the specified status
        """
        return [task for task in self.tasks if task.status == status]

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> bool:
        """
        Update a task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title
            description (str, optional): New description

        Returns:
            bool: True if task was updated, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            return False

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            if len(title) > 100:
                raise ValueError("Task title cannot exceed 100 characters")
            task.title = title.strip()

        if description is not None:
            if len(description) > 500:
                raise ValueError("Task description cannot exceed 500 characters")
            task.description = description.strip()

        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if task was marked complete, False if not found or already complete
        """
        task = self.get_task(task_id)
        if not task or task.status == "completed":
            return False

        task.mark_complete()
        return True
