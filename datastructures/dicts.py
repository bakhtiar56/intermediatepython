#Key-value pairs data structure , unordered and mutable

mydict={"name":"John","age":30,"salary":25000}
print (mydict)

mydict2=dict(name="John",age=30,salary=25000)#using dict()
value=mydict2.get("name")#get value of key
print(value)

mydict["email"]=["max@mx.com"]#add key-value pair

# del mydict["age"]#delete key-value pair
# mydict.pop("age")#also delete key-value pair
mydict.popitem()#delete last key-value pair

if "name" in mydict:#check if key is present
    print("Key is present")

try:
    print(mydict["name"])
except:
    print("Key is not present")

for keys in mydict:
    print (keys)
for keys,values in mydict.items():
    print(keys,values)
dict3=mydict.copy()#copy a dictionary
dict4=dict(name="Mary",age=25,salary=32300)#using dict()
mydict.update(dict4)#update a dictionary
print(mydict)

mytuple=(88,2)
mydictt={mytuple:21}#using dict()
print(mydictt)
mylist=[88,2]
mydictt={mylist:21}#throws error because list is mutable 
#not hashable