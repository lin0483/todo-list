# Python To-Do List

A simple command-line To-Do List application built with Python.

## Features

* Show all tasks
* Add new tasks
* Mark tasks as completed
* Delete tasks
* Persistent task storage using JSON

## Technologies

* Python
* JSON
* File Handling

## How to Run

Make sure Python is installed, then run:

```bash
python todo.py
```

The application stores tasks in a `tasks.json` file, allowing tasks to remain saved after closing the program.

## How It Works

Tasks are stored as dictionaries containing a title and completion status. The application uses JSON to save and load the task list from a local file.

## Project Structure

```text
python-todo-list/
│
├── todo.py
├── tasks.json
└── README.md
```

## Available Options

```text
1) Show tasks
2) Add task
3) Mark task as done
4) Delete task
5) Quit
```
