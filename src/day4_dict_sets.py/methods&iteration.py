marks = {"math": 80, "science": 75, "english": 85}

print(marks.get("math"))
print(marks.get("history", 0))

for subject, score in marks.items():
    print(subject, score)
