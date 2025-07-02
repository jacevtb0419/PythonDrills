course = {
    "Instructors": ["Steve Jobs", "Bill Gates"],
    "ID": {
        "Department": "CS",
        "Number": 1400
    },
    "Name": "Fundamentals of Computer Programming",
    "Assignments": {
        "Day 1": {
            "Points": 10,
            "Title": "Introduction"
        },
        "Day 2":{
            "Points": 5,
            "Title": "Installing Python"
        },
    }
}

print(course["Instructors"][0])
print(course["Assignments"]["Day 2"]["Title"])