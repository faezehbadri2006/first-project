count = int(input("Tedad dars-ha ra vared konid: "))
grades = []
for i in range(count):
    grade = float(input(f"Nomre-ye dars {i+1} ra vared konid: "))
    grades.append(grade)
average = sum(grades) / count
if average >= 12:
    print("Ghabool")
elif average >= 10:
    print("Mashroot")
else:
    print("Mardood")