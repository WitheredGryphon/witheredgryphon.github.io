'''
Given the names and grades for each student in a Physics class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.

Constraints:
2 <= N <= 5
'''

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    minScore = min(item[1] for item in students)
    students = list(filter(lambda x: x[1] != minScore, students))
    newMin = min(item[1] for item in students)
    findStudent = list(filter(lambda x: x[1] == newMin, students))
    print('\n'.join(sorted([findStudent[i][0] for i in range(len(findStudent))])))