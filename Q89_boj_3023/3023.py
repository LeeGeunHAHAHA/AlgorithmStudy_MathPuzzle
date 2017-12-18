from collections import deque as stack
st = stack()
r, c = map(int, input().split())
rows = [input() for i in range(r)]
a, b = map(lambda x: int(x)-1, input().split())
for i in range(r):
    tmp = list(rows[i])
    tmp.reverse()
    rows[i] = rows[i] + "".join(tmp)
for i in range(r):
    st.append(rows[i])
while st:
    rows.append(st.pop())
rows[a] = rows[a][:b] + ("#" if rows[a][b] == "." else ".") + rows[a][b+1:]
for i in rows:
    print(i)
