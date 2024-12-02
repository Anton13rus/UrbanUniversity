import statistics

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name_students = list(students)
name_students.sort()
#print(name_students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_sr = (statistics.mean(grades[0]),
             statistics.mean(grades[1]),
             statistics.mean(grades[2]),
             statistics.mean(grades[3]),
             statistics.mean(grades[4]))
#print(grades_sr)




sredniy_bal = zip(name_students, grades_sr)
print(dict(sredniy_bal))
