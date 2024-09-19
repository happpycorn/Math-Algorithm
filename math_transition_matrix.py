# 轉移矩陣模擬程式

x,y,p,q,t = map(float,input().split()) # 轉移矩陣數 1 , 轉移矩陣數 2 , 起始數 1 , 起始數 2 , 重複次數

t = int(t)

a,b = 0,0

for i in range(1,t+1):
    a = x*p + (1-y)*q
    b = (1-x)*p + y*q
    print("第",i,"年,",a,b)
    p = a
    q = b