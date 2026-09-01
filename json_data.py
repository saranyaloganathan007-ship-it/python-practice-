import json

student = {
    "name": "Saranya",
    "course": "Information Technology",
    "skill": "Python"
}

data = json.dumps(student)

print(data)