n = int(input())
student = list()
for i in range(n):
    student.append([input(), float(input())])

score = list(set([student[i][1] for i in range(len(student))]))
score.sort()
output = [x[0] for x in student if x[1] == score[1]]
output.sort()
for s in output:
    print(s)
