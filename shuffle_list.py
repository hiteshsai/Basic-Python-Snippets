import random
num = int(input('Size of elements : '))
arr = list()

for i in range(num) :
  ele  = int(input())
  arr.append(ele)

print(arr)


#students= ["Tom", "Harry", "David", "Greg", "Monroe"]
random.shuffle(arr)
print ("After shuffle -->")
print(arr)
