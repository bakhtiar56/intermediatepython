#Tuples are ordered, immutable , and contain duplicates
import sys
import timeit
mytuple=("a","b","c","d","e","Boston")
not_a_tuple=(123)#incorrect syntax for declaring a tuple of length 1
correct_tuple=(123,)#correct syntax for declaring a tuple of length 1
print(type(not_a_tuple))
print(type(correct_tuple))
list_to_tuple=tuple([1,2,3,4,5])
print(list_to_tuple[2])#normal indexing

print("Boston" in mytuple)#check if element is present in tuple

print(len(mytuple))#length of tuple
print(mytuple.count("a"))#count of element
print(mytuple.index("a"))#index of element

tuple_numbers=(1,2,3,4,5,6)
print(tuple_numbers[2:])#normal slicing
print(tuple_numbers[::-1])#reversing the tuple 

#Pattern Matching

tup=(1,"America","Europe",)
tup2=(1,2,3,4,5,6)
num,country,continent=tup#unpacking a tuple
i1,*i2,i3=tup2#unpacking a tuple, 
#every element between i1 and i2 is stored as a list
print (i2)

l1=[1,2,3,4,5,6]
t1=(1,2,3,4,5,6)
print("List has a size of:",sys.getsizeof(l1))
print("Tuple has a size of:",sys.getsizeof(t1))
#Tuples are more space efficient than lists

print(timeit.timeit(stmt="[1,2,3,4,5,6]",number=1000000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)",number=1000000)) 
#Tuples are faster than lists


