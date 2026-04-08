# a built in data type that let us create immutable sequences of value (not add or remove any number) and slicing is posible in tuple

#tup=(1,2,2,2,3,4)
#print(tup)
#print(type(tup))

#tup[0]=5   # not acceses because tuple is immutable


#print(tup[1:3])  # slicing in tuple


#print(tup.index(2))   # returns index of first index


#print(tup.count(2))   # counts total occurences


# Wap to ask the user to enter names of their 3 movies and store them in a list

#movies=[]
#movies.append(input("enter 1st movie name:"))
#movies.append(input("enter 2nd movie name:"))
#movies.append(input("enter 3rd movie name:"))
#print(movies)


# wap to check if a list contains a palindrome of elements

#list1=[1,2,3]
#copy_list1=list1.copy()
#copy_list1.reverse()
#if(copy_list1==list1):
 #   print("palindrone")
#else:
 #   print("not palindrone")