from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# ✅ Proper CORS Fix (solves "Failed to fetch")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow ALL origins
    allow_credentials=True,
    allow_methods=["*"],        # Allow ALL methods
    allow_headers=["*"],
)

students_data = []

# ✅ Read CSV File
with open("q-fastapi (1).csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students_data.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

# ✅ API Endpoint
@app.get("/api")
def get_students(class_: list[str] | None = Query(default=None, alias="class")):

    # Return ALL students if no filter
    if not class_:
        return {"students": students_data}

    # Filter students by class
    filtered_students = [
        student for student in students_data
        if student["class"] in class_
    ]

    return {"students": filtered_students}
