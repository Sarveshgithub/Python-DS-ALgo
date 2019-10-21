def sequence(seqList, quary, n):
    lastAnswer = 0
    for i in range(len(quary)):

        q, x, y = quary[i][0], quary[i][1], quary[i][2]
        # q1
        if q == 1:
            seq = (x ^ lastAnswer) % n
            seqList[seq].append(y)
            print(seqList)
        elif q == 2:
            seq = (x ^ lastAnswer) % n
            print(seq)
            lastAnswer = y % len(seqList[seq])
            print(seqList[seq][lastAnswer], seqList)


i1 = list(map(int, input().split(" ")))
n, q = i1[0], i1[1]
seqList = [[] for i in range(n)]
quary = []
for _ in range(q):
    quary.append(list(map(int, input().split(" "))))

sequence(seqList, quary, n)
