def count_1(list, z):
    count_2 = 0
    for i in range(z):
        count_2 += list[i].count(1)
    return count_2

def index_1(lsst: list, c):
    for i in range(0, c):
        if lsst[i].count(1) !=0:
            return [i, lsst[i].index(1)]

def without_1(list, m, n):
    for h in range(1, m-1, 2):
        for f in range(1, n-1, 2):
            if pole[h][f]==1 and pole[h-1][f]==0 and pole[h-1][f+1]==0 and pole[h][f+1]==0 and pole[h+1][f+1]==0 and pole[h+1][f]==0 and pole[h+1][f-1]==0 and pole[h][f-1]==0 and pole[h-1][f-1]==0:
                pole[h][f]=3
    if pole[0][0]==1 and pole[0][1]==0 and pole[1][1]==0 and pole[1][0]==0:
        pole[0][0]=3
    if pole[0][n-1]==1 and pole[0][n-2]==0 and pole[1][n-2]==0 and pole[1][n-1]==0:
        pole[0][n-1]=3
    if pole[m-1][0]==1 and pole[m-2][0]==0 and pole[m-2][1]==0 and pole[m-1][1]==0:
        pole[m-1][0]=3
    if pole[m-1][n-1]==1 and pole[m-1][n-2]==0 and pole[m-2][n-2]==0 and pole[m-2][n-1]==0:
        pole[m-1][n-1]=3
    for e in range(1, m-2):
        if pole[e][1]==0 and pole[e-1][1]==0 and pole[e+1][1]==0 and pole[e-1][0]==0 and pole[e+1][0]==0 and pole[e][0]==1:
            pole[e][0]==3
        if pole[e][n-2]==0 and pole[e-1][n-2]==0 and pole[e+1][n-2]==0 and pole[e-1][n-1]==0 and pole[e+1][n-1]==0 and pole[e][n-1]==1:
            pole[e][n-1]==3
    for v in range(1, n-2):
        if pole[0][v]==1 and pole[1][v]==0 and pole[1][v-1]==0 and pole[1][v+1]==1 and pole[0][v-1]==0 and pole[0][v+1]==0:
            pole[0][v]==3
        if pole[m-1][v]==1 and pole[m-2][v]==0 and pole[m-2][v-1]==0 and pole[m-2][v+1]==0 and pole[m-1][v-1]==0 and pole[m-1][v+1]==0:
            pole[m-1][v]=3
    return list

def index_1_in_regi(lst: list, lst2: list):
    minm = min([i[0] for i in lst])
    maxm = max([i[0] for i in lst])
    minn = min([i[1] for i in lst])
    maxn = max([i[1] for i in lst])
    for r in range(minm, maxm+1):
        for s in range(minn, maxn+1):
            if lst2[r][s]==1:
                return [r, s]
            
def find_square(llst: list, lst3 :list):
    minm = min([i[0] for i in llst])
    maxm = max([i[0] for i in llst])
    minn = min([i[1] for i in llst])
    maxn = max([i[1] for i in llst])
    squar = (maxn-minn+1)*(maxm-minm+1)
    count = 0
    for i in range(minm, maxm+1):
        for j in range (minn, maxn+1):
            if lst3[i][j] ==1 or lst3[i][j]==2 or lst3[i][j]==3:
                count +=1
    return [count/squar, squar]

def find_regi(lst: list, pole: list, m, n: int):
    switch = 1
    while switch:
        switch = 0
        for k in range(len(lst)):
            i = lst[k][0]
            j = lst[k][1]
            pole[i][j]=2
            if i > 0 and pole[i-1][j] == 1:
                lst.append([i-1,j])
                switch = 1
                pole[i-1][j]=2
            if j > 0 and pole[i][j-1] == 1:
                lst.append([i, j-1])
                switch = 1
                pole[i][j-1]=2
            if i > 0 and j > 0 and pole[i-1][j-1] == 1:
                lst.append([i-1, j-1])
                switch = 1
                pole[i-1][j-1] = 2
            if i < (m-1) and pole[i+1][j] == 1:
                lst.append([i+1, j])  
                switch = 1
                pole[i+1][j] = 2
            if j < (n-1) and pole[i][j+1] == 1:
                lst.append([i, j+1])
                switch = 1
                pole[i][j+1] = 2   
            if i < (m-1) and j < (n-1) and pole[i+1][j+1] == 1:
                lst.append([i+1, j+1])
                switch = 1
                pole[i+1][j+1] = 2
            if i < m-1 and j > 0 and pole[i+1][j-1] == 1:
                lst.append([i+1, j-1])
                switch = 1
                pole[i+1][j-1] = 2
            if i > 0 and j < n-1 and pole[i-1][j+1] == 1:
                lst.append([i-1, j+1])
                switch = 1
                pole[i-1][j+1] = 2
    return lst

 
line = []
line = input().split(' ')
n, m = line
n, m = int(n), int(m)
pole = []
for u in range (m):
    pole.append(list(map(int, input().split())))
pole = without_1(pole, m, n)
all_regiones = []
while count_1(pole, m) > 0:
    lstt = [index_1(pole, m)]
    region = find_regi(lstt, pole, m, n)
    squar = find_square(region, pole)
    if squar[1] > 2:    
        # if len(region) > 3:
        #     x_regi = [index_1_in_regi(region, pole)]
        #     # if x_regi ==None:
            #     break
            # else:
            #     region_2 = []
            #     region_2 = find_regi(x_regi, pole, m, n)
            #     if region_2 in region:
            #         squar_2 = find_square(region_2, pole)
            #         all_regiones.append([squar_2])
            #         all_regiones.append([squar])
            #     else:
            #         region.append(x_regi)
            #         region_3 = []
            #         region_3 = find_regi(region, pole, m, n)
            #         squar_3 = find_square(region_3, pole)
            #         all_regiones.append([squar_3])
        # else: 
        all_regiones.append(squar)                                  
if len(all_regiones) == 0:
    print(0)
elif len(all_regiones) == 1:
    print(all_regiones[0][1])
else: 
    max_effect = max(i[0] for i in all_regiones)
    max_squares = []
    for g in all_regiones:
        if g[0] == max_effect:
            max_squares.append(g[1])
    print(max(max_squares))