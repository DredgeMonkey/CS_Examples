last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physicis", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

gradebook = list(zip(grades, subjects))

print(gradebook);

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook);
