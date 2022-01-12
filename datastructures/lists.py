#python lists are ordered, mutable, and can contain duplicates

#to create a list,
l=list()
l1=[1,2,3,4,5]

#to access the elements of a list,
print(l1[0])


#Slicing

#to slice a list,where first number is beginning index
#and second number is ending index not included
print(l1[1:3])
#to get all elements of a list,
print(l1[1:])#get all elements starting from index 1

print(l1[::1])#start from index 0,step size 1 till end
print(l1[::2])#start from index 0,step size 2 till end
print(l1[::-1])#start from index 0,step size -1 till end i.e. 
#reversing the list

#Copying a list
l2=l1#l2 is a reference to l1

l3=list(l1)#l3 is a copy of l1
l4=l1.copy()#l4 is a copy of l1
l5=l1[:]#l5 is a copy of l1

#List Comprehension
squares=[x**2 for x in l1]



