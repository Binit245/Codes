#  dictionaries are used to store data values in key:value pairs
#  they are unordered,mutable(changeable) and do not allow duplicate keys

# simple example


'''info={
    "name" : "binit kumar",
    "subject": ["python", "math", "chemistry"],
    "topic": ("set", "dicctionary"),
    "course" : "b-tech",
    "age": 19
}
print(info, type(info))'''


# nested dictionary

'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
print(student)
print(student["subject"])
print(student["subject"]["python"])'''


# dictionary methods

# mydict.keys()   # return all keys

'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
print(student.keys())
print(list(student.keys()))
print(len(student))'''


# mydict.values()    # return all values


'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
print(student.values())
print(list(student.values()))'''


# mydict.items()     # return all (key,val) pairs as tuples


'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
print(student.items())
print(list(student.items()))
pairs=(list(student.items()))
print(pairs[0])'''


# mydict.get("key")    # returns the key according to value


'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
print(student.get("subject"))
print(student.get("name"))
print(student["name"])
#print(student["name2"])   # return (error)
#print(student.get("name2"))  #return(none)'''



# mydict.update(new dict)   # returns the specified items to the dictionary


'''student={
    "name": "binit kumar",
    "subject":{
        "che":87,
        "math":80,
        "python":95
    }
}
(student.update({"city": "nawada"}))
student.update({"name":"rahul"})
print(student)'''






'''from turtle import *

bgcolor("black")
pensize(2)
color("green")
left(90)
backward(100)
speed(200)
shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        forward(i)
        color("orange")
        circle
        color("brown")
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)
tree(100)
done()'''