                #  in the python class #


# mutable data type


'''test=(1,2,3,4,5,3,5,1,1,3)
list=[]
for ele in test:
    if(ele not in list):'''




# new code
'''test=(1,2,3,4,5,3,5,1,1,3)
temp=[]
for ele in test:
    if test.count(ele)==1:
        temp.append(ele)
newtest=tuple(temp)
print(newtest)'''

# new code
'''listt=[['tpl','listt'],['a',1],['roll','number']]  #convert a list of list to tuple of tuple
result=tuple(tuple(pair) for pair in listt)
print(result)'''

# count total times a word is occouring in a sentence
'''s="raman suman das raman das aarav parth aarav"
d={}
for name in s.split(" "):
    d[name]=d.get(name,0)+1
print(d)'''


# in a school,there are many students with same first names. task is to find the students with same names. 
# a string will be given comparising off all the names of students and you have to tell the name and count of those
# students having same name.
# 1) if all the names are unique,print-1 instead
# 2) no ned to mention names whose frequency is 1.

'''s="binit anurag alok abhiraj aditya"
d={}
for x in s.split(" "):
    d[s]=d.get(s,0)-1        ## not complete code
for x in d.keys():
    if d[x]>1:
           print(x,d[x])'''



# add the element of a list to a set

'''sample_set ={"yellow","orange","black"}
listt=["blue","green","red"]
sample_set.update(listt)
print(sample_set)
print(len(sample_set))'''


# print identical elements of two sets

'''set1={1,2,3,4,5}
set2={4,2,5,6,8}
identical_element=set1.intersection(set2)
print(identical_element)'''

# print all the elements of two sets
'''
set1={1,2,3,4,5}
set2={2,4,7,5,6}                 # operator for union('|')
identical_element=set1.union(set2)
print(identical_element)'''


# perform all set operations
'''
set1={1,2,3,4,5}
set2={2,4,5,6,7}               
identical_element=set1.difference(set2)
print(identical_element)'''

'''
set1={1,2,3,4,5}
set2={2,4,5,6,7}               
identical_element=set1.symmetric_difference(set2)
print(identical_element)'''

# check if a set is a super set of other set or not, print boolean result





                    
                    
                    
                    
                    
                    
                    
                     # by apna college #


    # set is the collection of unordered items
    
    # each element in the set must be unique and immutable(not add or remove any value)
    # in the list set and dictionary function do not acceptable
    # set is mutable but elements of the set is immutable


# simple example

'''collection={1,2,2,3,4,4,"hello","world"}
print(collection)                # in the set 2 and more value is count and it print only one time
print(type(collection))
print(len(collection))'''  # total no of items in one time


# create empty set

'''collection={}         # empty dictionary
print(type(collection))

collection=set()      # empty set
print(collection)
print(type(collection))'''



# set methods

# set.add(ele)    adds an element


'''collection={1,2,3,4}
collection.add(5)
print(collection)

collection= set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)'''


# set.remove(ele)    removes an element


'''collection= set()
collection.add(2)
collection.add(3)
collection.add(2)
collection.add(4)
collection.remove(2)
print(collection)'''

'''collection=set()
collection.add(1)
collection.add(2)
collection.add((1,2,3))
#collection.add([1,2,3])  this will not print because list is mutable
collection.add("apna college")
print(collection)'''


# set.clear


'''collection= set()
collection.add(2)
collection.add(3)
collection.add(2)
collection.add(4)
collection.clear()    # it will remove all element 
print(collection)'''

# set.pop

'''collection= {"apna","college","school","college","hostel"} 
print(collection.pop())  # it will remove any random value
print(collection.pop())'''


# set.union   (combines both set values and return new value)


'''set1={1,2,3,4}
set2={5,6,7,4,3}
print(set1.union(set2))'''


# set.intersection    (combines common value and return new value)

'''set1={1,2,3,4,5,6}
set2=(2,3,6,7,4)
print(set1.intersection(set2))'''


# QUESTION PRACTICE

# store following word meanings in a python dictionary

'''dict={
    "cat": "a small animal",
    "table": ["a piece of furniture","list of fact & fingure"]
}
print(dict)'''


# you are given a list of subject for studdents. assume one classroom is required foe 1 subject how many 
#calssrooms are needed by all students


'''subjects={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(len(subjects))'''


# wap to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary & store one by one use subject name as a key & marks as value


marks={}

'''x=int(input("enter phy :"))
marks.update({"phy": x})

x=int(input("enter che :"))
marks.update({"che": x})

x=int(input("enter python :"))
marks.update({"python": x})
print(marks)'''

# figure out a way to store 9 & 9.0 as seprete values in the set
# (you can take help of buiilt-in data types)


value={
    ("float",9.0),
    ("int",9)
}
print(value)