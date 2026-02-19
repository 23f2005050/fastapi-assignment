from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS (assignment requirement)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students_data = []

# Read CSV file
with open("q-fastapi (1).csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students_data.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
def get_students(class_: list[str] | None = Query(default=None, alias="class")):

    if not class_:
        return {"students": students_data}

    filtered_students = [
        student for student in students_data
        if student["class"] in class_
    ]

    return {"students": filtered_students}
