# 2060
a = int(input())
count=count1=count2=count3=0
b = list(map(int,input().split()))
for i in range(a):
    if b[i]%2 ==0:
        count+=1
    if b[i]%3 ==0:
        count1+=1
    if b[i]%4 ==0:
        count2+=1
    if b[i]%5 ==0:
        count3+=1
print(f'''{count} Multiplo(s) de {2}
{count1} Multiplo(s) de {3}
{count2} Multiplo(s) de {4}
{count3} Multiplo(s) de {5}''')