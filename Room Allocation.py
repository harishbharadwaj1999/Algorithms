#t=[[1,2],[2,4],[4,4]]
leave=[]
order=[]
c=0
for i in range(len(t)):
    if i==0:
        c+=1
        leave.append(t[i][1])
        order.append(i+1)
    else:
        f=0
        for j in range(len(leave)):
            if leave[j]<t[i][0]:
                f=1
                leave[j]=t[i][1]
                order.append(j+1)
                break
        if f==0:
            c+=1
            leave.append(t[i][1])
            order.append(len(leave))
print(c)
order=[str(i) for i in order]
print(''.join(order))
