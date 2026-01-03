# Todo Python Console App

A simple, efficient command-line todo application built with Python. Manage your tasks with ease through an intuitive console interface.

## 🎯 Features

- ✅ **Add Tasks** - Create new tasks with titles and optional descriptions
- 🗑️ **Delete Tasks** - Remove tasks with confirmation prompts
- ✏️ **Update Tasks** - Modify task titles and descriptions
- 👀 **View Tasks** - Display all tasks with filtering options (All, Pending, Completed)
- ✅ **Mark Complete** - Mark tasks as completed with timestamp tracking
- 📊 **Status Tracking** - Track task creation and completion dates

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- UV package manager (recommended)

### Installation

1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd todo-app
   ```

3. **Install dependencies** (if any):
   ```bash
   uv pip install -e .
   ```

### Running the Application

#### On Windows (PowerShell)
```powershell
# Navigate to the project directory
cd todo-app

# Run the application
python main.py
```

#### On Linux/macOS (Bash)
```bash
# Navigate to the project directory
cd todo-app

# Run the application
python main.py
```

## 📖 Usage

The application presents a menu-driven interface:

```
==================================================
📋 TODO APP MENU
==================================================
1. ➕ Add Task
2. 🗑️  Delete Task
3. ✏️  Update Task
4. 👀 View Tasks
5. ✅ Mark Task Complete
6. 🚪 Exit
==================================================
```

### Adding a Task
1. Select option `1`
2. Enter a task title (required)
3. Enter a description (optional)
4. Task is created with a unique ID

### Deleting a Task
1. Select option `2`
2. Enter the task ID
3. Confirm deletion
4. Task is permanently removed

### Updating a Task
1. Select option `3`
2. Enter the task ID
3. Modify title and/or description
4. Changes are saved

### Viewing Tasks
1. Select option `4`
2. Choose a filter:
   - All tasks
   - Pending tasks
   - Completed tasks

### Marking Complete
1. Select option `5`
2. Enter the task ID
3. Task status changes to completed

## 🏗️ Architecture

### Project Structure
```
todo-app/
├── main.py                 # Application entry point
├── todo_app/              # Main package
│   ├── __init__.py       # Package initialization
│   ├── tasks.py          # Task model and TaskManager
│   └── cli.py            # Command-line interface
├── specs/                 # Specifications and documentation
│   └── todo-app/
│       ├── spec.md       # Functional requirements
│       ├── plan.md       # Architectural decisions
│       └── tasks.md      # Implementation tasks
├── history/               # Prompt History Records
└── README.md             # This file
```

### Key Components

- **Task**: Data model representing a todo item
- **TaskManager**: Business logic for task operations
- **TodoCLI**: User interface and command handling

## 🔧 Technical Details

- **Language**: Python 3.13+
- **Storage**: In-memory (no persistent storage)
- **Package Manager**: UV
- **Code Style**: PEP 8 compliant
- **Architecture**: Modular with separation of concerns

## 📋 Development

This project follows **Spec-Driven Development (SDD)** methodology:

1. **Constitution** - Project principles and constraints
2. **Specifications** - Detailed functional requirements
3. **Implementation Plan** - Architectural decisions
4. **Tasks** - Testable implementation steps
5. **Code** - Actual implementation
6. **Testing** - Verification and validation

### Running Tests

```bash
# Manual testing
python main.py

# Test individual components
python -c "from todo_app.tasks import TaskManager; tm = TaskManager(); print('TaskManager imported successfully')"
```

## 🤝 Contributing

1. Follow the established Spec-Driven Development workflow
2. Ensure PEP 8 compliance
3. Add comprehensive docstrings
4. Test thoroughly before submitting changes

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🆘 Support

If you encounter issues:
1. Check that Python 3.13+ is installed
2. Ensure all files are in the correct directory structure
3. Verify no syntax errors in the code
4. Check the specifications and implementation plan for expected behavior

## 📚 Documentation

- [Specifications](specs/todo-app/spec.md) - Detailed requirements
- [Implementation Plan](specs/todo-app/plan.md) - Architecture decisions
- [Tasks](specs/todo-app/tasks.md) - Implementation breakdown
- [Constitution](.specify/memory/constitution.md) - Project principles

---

**Built with ❤️ using Spec-Driven Development**
