# a = list()
# for i in range(3):
#     a.append([input(), float(input())])
# print(a)
student = [["sss", 1.3], ["dfff", 3.3], ["sarvesh", 5.3], ["Lokesh", 2.3], ["lll", 2.3]]

score = list(set([student[i][1] for i in range(len(student))]))
score.sort()
output = [x[0] for x in student if x[1] == score[1]]
for s in output:
    print(s)
