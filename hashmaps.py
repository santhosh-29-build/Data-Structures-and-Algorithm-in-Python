
student = {"name": "Arun", "age": 17}

print(student.get("name"))       
print(student.get("age"))       
print(student.get("city"))      
print(student.get("city", "Chennai"))  
d=student.copy()

for key,value in student.items():
    print(key,value)
print(d)