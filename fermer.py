line = []
line = input().split()
m, n = line
m, n = int(m), int(n)
basa = []
ones_basa = []   # список координат единичек
ones_border = []  # это список единицек по краю, пригодится 
for i in range (m):
    basa.append(list(map(int, input().split())))
    for j in range(n):
        if basa[i][j]==1:
            ones_basa.append((i, j))
            if (i == 0 or i == m-1 or j == 0 or j==n-1):
                ones_border.append((i,j))
print(basa, ones_basa, ones_border)


