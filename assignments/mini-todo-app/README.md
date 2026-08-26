# 📘 Assignment: Mini To-Do App with a Python API

## 🎯 Objective

Build a small Python application that serves a simple to-do list API and allows users to create, view, update, and complete tasks through HTTP requests.

## 📝 Tasks

### 🛠️ Build the API Foundation

#### Description
Create a Python script that runs a basic web API for managing tasks. The API should store tasks in memory and respond with JSON data.

#### Requirements
Completed program should:

- Use Python's built-in networking tools to run a simple web server
- Store tasks in a list or dictionary while the program is running
- Support a route to list all tasks
- Support a route to add a new task
- Return JSON responses for successful operations

### 🛠️ Add Task Management Features

#### Description
Expand the API so students can update a task's status and remove completed items.

#### Requirements
Completed program should:

- Allow a task to be marked as complete or incomplete
- Support deleting a task by ID
- Return a clear message when a task is not found
- Include a route for fetching a single task by its ID
- Continue to return valid JSON responses for each action

### 🛠️ Improve the User Experience

#### Description
Make the API easier to use by adding a few practical behaviors for a real to-do list.

#### Requirements
Completed program should:

- Validate incoming data such as title and status
- Reject empty or invalid task titles
- Keep task IDs unique
- Display a summary such as total tasks or number of completed tasks
- Use clear HTTP status codes like `200`, `201`, and `404`

### 🛠️ Optional Front-End Demo

#### Description
Create a tiny front-end page that sends requests to the API and displays the tasks in the browser.

#### Requirements
Completed program should:

- Create a simple HTML page with a task form
- Use JavaScript to fetch tasks from the API
- Display each task with its title and completion status
- Allow the user to add, complete, or delete tasks from the page
- Demonstrate how the browser and Python API work together
