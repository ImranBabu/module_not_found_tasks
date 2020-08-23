a = [1,2,3,4,6,3,2,1,0,6]
b = 0
p1 = 0
p2 = 0
balls_pla = []
temp = '1'
for i in a:
    b = b+1
    balls_pla.append(temp)
    if temp == '1':
        p1 += i
    else:
        p2 += i
    if b%6 == 0:
        if i%2 == 0:
            if temp == '1':
                temp = '2'
            else:
                temp = '1'
        else:
            if temp == '1':
                temp = '1'
            else:
                temp = '2'
    
    elif i%2 == 1:
        if temp == '1':
            temp = '2'
        else:
            temp = '1'
    '''elif i%2 != 1:
        if temp == '1':
            temp = '1'
        else:
            temp = "2"'''

for i in range(len(a)):
    print("player : ",balls_pla[i], " runs : ",a[i], " ball : ",i + 1)
print("player 1 : ",p1)
print("player 2 : ",p2)
