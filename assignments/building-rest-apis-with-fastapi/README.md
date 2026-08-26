# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating routes, validating request data, and managing in-memory resources for a small application.

## 📝 Tasks

### 🛠️ Create Your First API Endpoint

#### Description
Set up a FastAPI app and create a basic route that returns a welcome message or a list of sample data.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Create a GET route such as `/` or `/items`
- Return JSON data from the endpoint
- Run the app locally with Uvicorn or FastAPI's development server

### 🛠️ Add Request Validation

#### Description
Create a route that accepts input from the client and validates the data before processing it.

#### Requirements
Completed program should:

- Define a request model using `BaseModel`
- Accept JSON data in a POST request
- Validate required fields such as `name`, `price`, or `email`
- Return a response containing the submitted data
- Handle invalid input with a clear validation error from FastAPI

### 🛠️ Build a Small CRUD API

#### Description
Create a small API that can create, read, update, and delete records in memory.

#### Requirements
Completed program should:

- Implement at least four routes: `GET`, `POST`, `PUT`, and `DELETE`
- Store data in a Python list or dictionary while the app is running
- Return JSON responses for each operation
- Allow a client to add a new item and retrieve or update the stored data
- Include a clear response when a resource is not found

### 🛠️ Add a Realistic API Feature

#### Description
Enhance the API with a feature that makes it feel more like a real-world service.

#### Requirements
Completed program should:

- Add a useful endpoint such as filtering by ID, searching by name, or listing all records
- Use query parameters or path parameters in a meaningful way
- Return status codes such as `200`, `201`, or `404`
- Keep the code organized with clear route names and reusable data models
