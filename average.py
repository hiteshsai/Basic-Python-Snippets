num=int(input('how many number you want to compute average : '))

a=[]

for i in range(0,num):
    elements=int(input('Enter element :'))
    a.append(elements)

avg = sum(a)/float(num)

print('Average of the list is: ',avg)
