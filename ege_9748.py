with open('17_9748.txt') as f:
    A = [int(i) for i in f]
max_num = 0
for i in sorted(A)[::-1]:
    if i % 100 == 15:
        max_num = i
        break
B = []
for i in range(len(A) - 2):
    s = (len(str(abs(A[i]))) == 4) + (len(str(abs(A[i + 1]))) == 4) + (len(str(abs(A[i + 2]))) == 4)
    if s == 1 and A[i] + A[i + 1] + A[i + 2] >= max_num:
        B.append(A[i] + A[i + 1] + A[i + 2])
print(len(B), max(B))