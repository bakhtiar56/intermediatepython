#Unordered, mutable, and no duplicates

#To create a set
myset={1,2,4}
myset2=set()#creating empty set
myset3=set([1,2,3,4,5])#creating set from list

#To add an element to a set
myset.add(5)
myset.add(2)
myset.add(22)

#To remove an element from a set
myset.remove(2)
myset.remove(5)#throws error if element is not present

myset.discard(2)#does not throw error if element is not present
myset.clear()#empties the set
print(myset3.pop())#removes and returns the element

for i in myset3:
    print(i)

odds={1,3,5,7,9}
evens={2,4,6,8,10}
primes={2,3,5,7}

print(odds.union(evens))#union of two sets
print(odds.intersection(evens))#intersection of two sets
print(odds.difference(primes))#difference of two sets 
print(odds.symmetric_difference(primes))#symmetric difference of two sets i.e. XOR

setA={1,2,3,4,5}
setB={4,5,6,7,8}
setA.update(setB)#update setA with setB elements, no duplicates
setA.intersection_update(setB)#the same as setA=setA.intersection(setB)
setA.difference_update(setB)#the same as setA=setA.difference(setB)


#To check if a set is a subset of another set
print(setA.issubset(setB))#checks if setA is subset of setB
print(setA.issuperset(setB))#checks if setA is superset of setB
print(setA.isdisjoint(setB))#checks if setA and setB have no common elements

#To copy a set
setC=setA.copy()
setD=set(setB)

#Frozen Set
#Immutable set, unordered, and no duplicates
a=frozenset({1,2,3,4,5})#frozen set can be modified
