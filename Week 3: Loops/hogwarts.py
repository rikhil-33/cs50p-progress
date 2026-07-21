students = [
    {"name": "Adi", "location": "Delhi", "stream": "ECE"},
    {"name": "suri", "location" : "Hyd", "stream" : "Chem"},
    {"name": "Sreek", "location" : "AP", "stream" : "CSE"},
    {"name": "Yash", "location" : "Hyd", "stream" : None}
]

for student in students:
    print(student["name"], student["location"], student["stream"], sep=", ")