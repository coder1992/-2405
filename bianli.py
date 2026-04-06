mylist=[1,2,3,4,5,6,7,8,9,10]
mylist1=[]
mylist2=[]
ind=len(mylist)
i=0
while i<ind:
    if mylist[i]%2==0:
         mylist1.append(mylist[i])
    i+=1
print(f'通过while循环，从[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表{mylist1}。')

for i in mylist:
    if i%2==0:
        mylist2.append(i)
print(f'通过for循环，从[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表{mylist2}。')
