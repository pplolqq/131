cent = (310,420,270)
centx = cent[0] + cent[1]//2

l=[
(105,230,210),
(10,230,270),
(160,290,335)
]
res = []
for pos in l:
    x,y,z = pos[0],pos[0]+pos[1],pos[2]
    res.append([x,y,z])
l2 = []
for pos in l:
    x= 2*centx - pos[0] - pos[1]
    y = x + pos[1]
    z = pos[2]
    res.append([x,y,z])
pos = cent
x,y,z = pos[0],pos[0]+pos[1],pos[2]

res.append([x,y,z])
print(res)