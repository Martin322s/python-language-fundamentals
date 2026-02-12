student_info = input()
university = {}

while True:
    if ":" not in student_info:
        break
    
    name, id, course = student_info.split(":")
    course = course.replace("_", " ")
    
    if course not in university:
        university[course] = {}
    
    university[course][name] = int(id)

    student_info = input()

searched_course = student_info.replace("_", " ")

if searched_course in university:
    for key, value in university[searched_course].items():
        print(f"{key} - {value}")
