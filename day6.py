#Bubble sort
# arr=list(map(int,input().split()))
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[i]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)

#selection sort
# arr=list(map(int,input().split()))
# min_ind=arr[0]
# for i in range(0,len(arr)):
#     min_ind=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[min_ind]:
#             min_ind=j
#     arr[i],arr[min_ind]=arr[min_ind],arr[i]
# print(arr)

#insertion sort
# arr=[10,40,30,20,50]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#         arr[j+1]=key
# print(arr)

# 
# l=[3,2,6,4,1,5,7]
# l.sort()
# res=[]
# for i in l:
#     if i%2!=0:
#         res.append(i)
#     else:
#         res.insert(0,i)
# print(res)
# 
# l=[3,2,6,4,7,1,5]
# l.sort()
# print(l[-1])

# l=[3,2,6,4,7,1,5]
# max1=0
# for i in l:
#     if i>max1:
#         max1=i
# print(max1)

# l=[3,2,6,4,7,1,5]
# max1=0
# for i in l:
#     if i>max1:
#         max1=i
# max2=0
# for i in l:
#     if i>max2 and i!=max1:
#         max2=i
# print(max2)

# l=[3,2,6,4,7,1,5]
# k=4
# n=len(l)
# for i in range(k):
#     for j in range(0,n-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[-k])

#input:[[1,2],[5,1],[2,4],[6,3]] output:[[1,2],[2,4],[5,1],[6,3]]
# a=[[1,2],[5,1],[2,4],[6,3]]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i][0]<a[j][0] and a[i][1]>a[j][1]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# a=[[20,12,7],[10,5,22],[16,7,30]]
# for i in range(len(a)):
#     for j in range(0,len(a)-1-i):
#         if a[j][0]>a[j+1][0]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

#Arrange prime based on Ascending order 
# def prime(x):
#     for i in x:
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 break
#             return i
#     return None
# l=[[20,12,11],[10,5,22],[16,7,30]]
# b=[]
# n=len(l)
# for i in l:
#     b.append(prime(i))
# for i in range(n):
#     for j in range(0,n-i-1):
#         if b[j]>b[j+1]:
#             b[j],b[j+1] = b[j+1], b[j]
#             l[j], l[j + 1] = l[j+1],l[j]
# print(l)






