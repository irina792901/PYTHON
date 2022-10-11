line = []
line = input().split(' ')
n, m, s = line
n, m, s = int(n), int(m), int(s)
list_n = []
list_m = []
k = max(n, m)
sum_n = 0
count_n = 0
sum_m = 0
count_m = 0
switch1 = 1
switch2 = 1
for k in range(k):
    a, b = input().split(' ')
    if switch1:
        if a =='-' or s < sum_n + int(a) or count_n >= n:
            switch1 = 0
        else:
            a = int(a)
            sum_n += a
            count_n += 1
            list_n.append(a)
    if switch2:
        if b =='-' or s < sum_m + int(b) or count_m >=m:
            switch2 = 0
        else:
            b = int(b)
            sum_m += b
            count_m +=1
            list_m.append(b)
if count_n==0 or count_m ==0:
    if count_n ==0 and count_m == 0:
        print(0)
        exit()
    elif count_n==0:
        print(count_m)
        exit()
    else:
        print(count_n)
        exit()
length = [count_n, count_m]
j = 0
for i in range(count_n):
    while count_m > j and sum_n + list_m[j] <= s:
        sum_n += list_m[j] 
        j += 1
        if j == count_m:
            break
    length.append(count_n -i + j)
    sum_n -= list_n[count_n-i-1]                  
print(max(length))    
