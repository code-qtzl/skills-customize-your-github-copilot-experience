from fastapi import FastAPI

app = FastAPI(title="Student API")

# Sample in-memory data
students = [
    {"id": 1, "name": "Ava", "grade": "A"},
    {"id": 2, "name": "Leo", "grade": "B"},
]


@app.get("/")
def home():
    return {"message": "Welcome to the Student API!"}


@app.get("/students")
def get_students():
    return students
