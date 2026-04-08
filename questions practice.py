'''string1="abcefrtyu"
string2="qwertyrty"
set1=set(string1)
set2=set(string2)
identical_element=set1.difference(set2)
print(identical_element)'''

'''set1={1,2,3,4}
set2={3,4,5,6,7}
#set1=set(set1)
#set2=set(set2)
all_element=set1.union(set2)
print(all_element)'''


'''set1={1,2,3,4,5}
set2={2,3,4,5,6}
#set1=set(set1)
#set2=set(set2)
common_element=set1.intersection(set2)
print(common_element)'''

'''set1={1,2,3,4,5}
set2={2,3,4,5,6}
elements=set1.symmetric_difference(set2)
print(elements)'''


'''length=int(input())
breadth=int(input)
area_perimetr=2*length+breadth
print(area_perimeter)'''



#  ord() change of a character to ASCII value 
#  chr() change of a integer to character value
# ASCII= (a=97,b=98,c=99)



'''def ascii():
    str=input("my string is:")
    s=0
    for i in str:
        s+=ord(i)
    print(s)
y=ascii()'''
  

'''word="pytyhon programing"
n=len(word)
word1=word.upper()
word2=word.lower()
converted_word=""
for i in range(n):
    if(i%2==0):
        converted_word+=word2[i]
    else:
        converted_word+=word1[i] 
    print(converted_word)'''


'''number=int(input("enter a number"))
if number % 5 == 0 and number % 7 == 0:
    print("DIV")
else:
    print("ND")'''



'''# Input: Word spoken by Tarun's sibling
original_word = input("Enter the original word: ")

# Input: Word spelled by Roshan
reversed_word = input("Enter the word spelled by Roshan: ")

# Check if Roshan's spelling is the reverse of the original word
if original_word[::-1] == reversed_word:
    print("Correct! Roshan spelled the word in reverse.")
else:
    print("Incorrect! Roshan did not spell the word in reverse.")'''


'''n=input()
ascii=""
for i in range(len(n)):
    a=n[i]
    if i%2==0:
        ascii+=chr(ord(a)-2)
    else:
        ascii+=chr(ord(a)+2)
print(ascii)'''


# Input: List of product prices
'''print("Enter the prices of the products (comma-separated):")
product_prices = list(map(float, input().split(',')))

# Calculate total amount
total_amount = sum(product_prices)

# Determine the tax rate and calculate tax
if total_amount < 1000:
    tax_rate = 0.10  # 10%
    purchase_tax = 0
elif 1000 <= total_amount <= 9999:
    tax_rate = 0.15  # 15%
    purchase_tax = 0
else:
    tax_rate = 0.20  # 20%
    purchase_tax = 0.02  # 2% extra purchase tax

# Calculate tax amount and bill amount
tax_amount = total_amount * tax_rate
purchase_tax_amount = total_amount * purchase_tax
bill_amount = total_amount + tax_amount + purchase_tax_amount

# Display the bill in the required format
print("\nBill Details:")
print(f"Total Amount: {total_amount:.2f}")
print(f"Tax Amount: {tax_amount + purchase_tax_amount:.2f}")
print(f"Bill Amount: {bill_amount:.2f}")'''

'''a,b=map(int,input().split())
total=a*b
if total<1000:
    c=(10/100)*total
    d=total+c
    print(total,(c),(total+c))
elif(total>999 and total<10000):
    f=(15/100)*total
    s=total+f
    print(total,int(f),int(total+f))
elif(total>9999):
    h=(20/100)*total
    i=total+h
    o=(2/100)*i

    print(total,int(h+o),int(total=h+o))'''



# swapping of two numbers
'''a=int(input("enter a value"))
b=int(input("enter a value"))
print("befor swapping a=",a,"and b=",b)
temp=a
a=b
b=temp
print("after swapping a=",a, "and b=",b)'''


'''purposal=input("enter puposal:")
for i in range(1,1001,1):
    print(purposal,end=" ")'''


# print in reverse order
'''for i in range(10,0,-1):
    print(i)'''


'''ch=input("enter ur choice in form of h and v:")
if(ch=='h'):
    for i in range(1,51,3):
        print(i,end=" ")
elif(ch=='v'):
    for i in range(1,51,3):
        print(i)
else:
    print("invalid choice")'''


# find factorial of a number
'''n=int(input("enter a number"))
fact=1
for i in range(1,n+1,1):
    fact*=i
print("factorial is :", fact)'''



'''wish =input("enter wish:")
i=1
while(i<=1001):
    i+=1
    print(wish,end=" ")'''