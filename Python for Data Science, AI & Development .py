#!/usr/bin/env python
# coding: utf-8

# # Python Basic Notebook 

# In[1]:


print ("Hellow world")


# ## Data Types

# In[2]:


type (3)


# In[3]:


type (4)


# In[4]:


type (5.3)


# In[5]:


type (6.3333)


# In[6]:


type ("I am learning python")


# In[7]:


type ("hellow word")


# ### boolean

# In[8]:


True 


# In[9]:


type (True)


# In[10]:


False 


# In[11]:


type (False)


# In[12]:


int(True)


# In[13]:


int(False)


# In[14]:


bool(0)


# In[15]:


bool(1)


# ### Type casting 

# In[16]:


int (4.33)


# In[17]:


int (4.0)


# In[18]:


float (3)


# In[19]:


str (4)


# In[20]:


str(4.55)


# In[21]:


type(True)


# In[22]:


int(True)


# In[23]:


bool(1)


# In[24]:


int(False)


# In[25]:


bool(0)


# In[26]:


bool(5)


# In[27]:


bool(-3)


# ### variables in python

# In[28]:


x_value = 45


# In[29]:


print (x_value)


# In[30]:


y = x_value + 47
y


# In[31]:


print (y)


# In[32]:


x_value = x_value/3


# In[33]:


x_value


# In[34]:


print (x_value)


# ### Expression and Variables

# In[35]:


5+3+5+89


# In[36]:


98*8


# In[37]:


34+76-34


# In[38]:


(3+3)*4


# In[39]:


37/2


# In[40]:


37//2


# In[41]:


print("Hellow , world") #Print the traditional hello world


# In[42]:


print(" Michael Jackson \n is the best" )


# In[43]:


Name = "tahir " 
Name = Name + "husain"
Name


# In[44]:


print ("you can call \t me professor")


# ## converting into upper case

# In[45]:


a = "hey, professor here!"
print ("before upper case:",a)
b = a.upper()
print ("after upper case:",b)


# In[46]:


a = "I love you so much baby"
b= a.upper()
b


# In[47]:


C = "MONEY HEIST"
D = C.lower()
D


# In[48]:


e = "I am Tahir ,but you can call me professor"
f = e.upper()
f


# In[49]:


g = f.replace("TAHIR","Berline")
g


# ## find substring

# In[50]:


my_name = "my name is khan"


# In[51]:


my_name.find("Khan")


# ## slicing

# In[52]:


my_name[0:8]


# In[53]:


my_name[0:10:2]


# ## List 

# In[54]:


my_list = [2,3.4,"Professor"]
type(my_list)


# In[55]:


print(my_list[0])
print(my_list[1])
print(my_list[2])


# In[56]:


print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))


# In[57]:


my_list[2]="Tahir"


# In[58]:


my_list[0]="Moneyheist"


# In[59]:


my_list


# In[60]:


my_list1 = [2,4.4,("money" ,"heist"),"professor",(3,4,7.2)]


# In[61]:


type(my_list1)


# In[62]:


my_list1[4]


# In[63]:


my_list1[3]


# In[64]:


my_list1[4][2]


# In[65]:


my_list1[4][0]


# In[66]:


type(my_list1[4][2])


# ## Insert and append in List

# In[67]:


my_list1.insert(0,420)
my_list1


# In[68]:


my_list1.append("khalid")


# In[69]:


my_list1


# In[70]:


my_list


# In[71]:


my_list.append(45)
my_list


# In[72]:


listrndm =[41, 21.3, 55, 4.444, "tahir","muhammad"]
listrndm


# In[73]:


listrndm.append(7)
listrndm


# In[74]:


listrndm.insert(7,5,8)  #insert takes two element max


# In[75]:


listrndm.insert(4,"husain") 
listrndm


# In[76]:


Q = [4,5,6,2,3,5,8,9,5]
P = Q[:]        # making duplicate of list


# In[77]:


print(Q)
print(P)


# ## del and remove items from list 

# In[78]:


my_list


# In[79]:


my_list.remove("Moneyheist")
my_list


# In[80]:


my_list1


# In[81]:


my_list1.remove(420)
my_list1


# In[82]:


del my_list[0]
my_list


# In[83]:


del my_list1[0]
my_list1


# In[84]:


my_list1


# In[85]:


del my_list1[1]
del my_list1[2]


# In[86]:


my_list1


# # Tuple

# In[87]:


my_tuple = (23,22.33,"Professor")
type(my_tuple)


# In[88]:


my_tuple[0]


# In[89]:


my_tuple[-1]="Tahir" #we can't change the tuple items , tuples are immutable 


# In[90]:


my_tuple1=list(my_tuple) #conveting tuples into list
#now we can change the items as tuple has been conveted into list 
my_tuple1[-1] = "Tahir" # changig items
tuple(my_tuple1) #agin changing into tuple
my_tuple1


# In[91]:


type(my_tuple1)


# In[92]:


type(tuple(my_tuple1))


# In[93]:


tuple1=(23,3,45,4.5,45,4.3,2,3,1,)
type(tuple1)


# In[94]:


tuple2=(98,9.0,8.998)
type(tuple2)


# In[95]:


tuple3=tuple1+tuple2 # adding two tuples as two tuples can be added  
tuple3


# In[96]:


sorted(tuple3) #sorting tuple


# In[97]:


print(tuple3)


# In[98]:


print(sorted(tuple3)) #sorting tuple


# In[99]:


tuple3[0:4]  #slicing print of tuple


# In[100]:


tuple3[0:11:3]    #slicing print of every 3rd item of the tuple3 


# ### Nesting tuple 
# #### tuples under a tulple 

# In[101]:


nestedtp = (23,2.3,34,"Tahir",("money","professor"),45,50,("love","ajkal"))    #nested tuple 
nestedtp


# In[102]:


nestedtp[-1]


# In[103]:


nestedtp[0]


# In[104]:


nestedtp[-1][-1]


# In[105]:


nestedtp[4][0]


# In[106]:


nestedtp[4][-1]


# In[107]:


nestedtp.index("Tahir")   # finding index of the tuple's items


# In[108]:


nestedtp.index(23)


# ## Dictionay in Python

# In[109]:


# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.


# In[110]:


my_dictionary = {"heist":2021, "GOT":2015, "Lord of the rings":2003, "harry":2009, "hritik":"superstar", "shahrukh":"king khan"}


# In[111]:


print(my_dictionary)


# In[112]:


my_dictionary["heist"]


# In[113]:


type(my_dictionary)


# In[114]:


my_dictionary["Salman"]= "Dabang"  #adding item to the dictonary 


# In[115]:


my_dictionary


# In[116]:


"Salman" in my_dictionary   #varifying  


# In[117]:


"GOT" and "harry" in my_dictionary  #varifying the items in the dic 


# In[118]:


my_dictionary.keys() #get all the keys in the dictionary


# In[119]:


my_dictionary.values()  #get all the values in the dictonary 


# In[120]:


print(my_dictionary)


# In[121]:


del my_dictionary["GOT"] #deleting the item form dic
my_dictionary


# # Set 

# #### A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets . Python will automatically remove duplicate items:
# 

# In[122]:


my_set = {"tahir", "professor", "money", 21, 12.55, False, "tahir", "professor"}   #creating a set 
type(my_set)


# In[123]:


print(my_set)   # set collect only unique value ,see the bellow all the duplicates has been removed 


# In[124]:


new_list = ["tahir","professor",21, False]  #this is a list 
type(new_list)


# In[125]:


new_set = set(new_list)  # converting new_list into a set 
type(new_set)


# #### adding , remove  in set:

# In[126]:


my_set.add("husain")   #adding items into set 
my_set


# In[127]:


new_set.add("husain")
new_set


# In[128]:


"husain" in new_set #varifying the elements 


# In[129]:


my_set.remove(False) #removing an elements from our set
my_set


# In[130]:


new_set.remove(False)
new_set


# ###  subset,intersection and union 

# In[131]:


set3 = {"tahir","husain"}
set3


# In[132]:


print(my_set)
print(new_set)


# In[133]:


my_set - new_set   #subtraction


# In[134]:


set3.issubset(my_set) #checking of subset


# In[135]:


set3.issubset(new_set)


# In[136]:


set3.issubset(my_set and new_set)


# In[137]:



my_set.intersection(new_set)   #checking intersecton


# In[138]:


my_set & new_set # we can also check intersection by & 


# In[139]:


new_set.intersection(my_set)


# In[140]:


my_set.union(new_set)


# In[141]:


my_set | new_set # other way to find union 


# In[142]:


my_set.union(new_set and set3)


# In[143]:


my_set | new_set | set3  # or 


# In[144]:


new_set.union(set3)


# In[145]:


new_set.union(my_set,set3)


# # if ,elif , else function 
# #### for eqal (==), for not equal (!+=) ,greater than (>) , less than (<), greater than or equal (>=), less than or equal (<=)

# In[146]:


a1 = 3
a3 = 4
a2 = 5 
a4 = 3


# In[147]:


a1>a2


# In[148]:


a3<a4


# In[149]:


a1==a4


# In[150]:


a1!=a4


# In[151]:


a1>=a4


# In[152]:


rating = 8.5
if rating>8.5:
    print("movie is amazing")
else:
    print("movie is ok")


# In[153]:


age = 20
if age>18:
    print("you can watch this movie")
else:
    print("you can't watch this movie")
print ("Good, Bye")


# In[158]:


age = int(input("Enter your age:",))
if age>=18:
    print("you can drive")
else:
    print("you can't drive")     # if and else is for two condition only
    


# In[155]:


Marks_percentage = float(input("Enter your percentage:",))      ## if , elif and else used for the multiple condition 
if Marks_percentage>=60:
    print("passed with first division")
elif Marks_percentage>=45:
    print("passed with secound division")
elif Marks_percentage>=33:
    print("passed with third division")
else:
    print("fail")


# ### for loop 
# #### when we know the number if iteration then we prefer for loop 

# In[156]:


for i in range(10):
    print(i)


# In[157]:


for i in range (1,101):    #writing count 1 to 100
    print(i)


# In[159]:


for i in range(2,21,2):  #writing table of 2 
    print(i)


# In[160]:


for i in range (79,791,79): #writing table of 79
    print(i)


# In[161]:


for i in range (956512,9565121,956512): # table of 956512 on jitu demond 
    print(i)


# In[162]:


colour = ["red", "pink", "white", "Yellow", "Ghreen", "Black"]
for i in colour:
    print(i)


# In[163]:


E = ('a', 'b', 'c', 'd', 'e')
for i in E:
    print(i, "is a small letter")


# In[164]:


E1 = ["A", "B" ,"C", 'D']
for i in E1:
    print(i,"a")


# In[165]:


E2 = ["A", "B" ,"C", 'D']            # enumerate gives idex and value both 
for i,x in enumerate(E2):
    print(i,x)


# In[166]:


E3 = ['rahul','suraj','mamta','sonu','sandeep']
for i,x in enumerate(E3):                        #by using enumerate 
    if i%2==0:
        print(x)
    


# ### f strings

# In[167]:


E3 = ['rahul','suraj','mamta','sonu','sandeep']    # f" strings , varriale must be in {} 
for i,x in enumerate(E3):
    if i<=2:
        print(i,f"this is the topper of our batch {x}")


# ### while loop 
# when we don't know the no. of iteration then we use while loop 

# In[168]:


i = 1 
while i<=10:
    print (i)   # this is how to write count in while loop 
    i=i+1


# In[169]:


i=2
while i<=20:   # writng table of 2 using while loop
    print(i)
    i=i+2


# In[170]:


while True:
    user_name = input("Enter your user name",)    # Enter user name interface by using alpha 
    if user_name.isalpha():
        print("user name ",user_name)              #must use break in this condition to avoid error
        break
    else:
        print ("user name can't be integer")


# In[171]:


while True:
    user_id = input("enter your user id:",)
    passwordd = int(input("enter your password"))            ## user and password block created using while loop 
    if user_id == "tahir123" and passwordd == 12345:
        print("login seccessful")
        break
    else:
        print("incorrect user id or password try again!")


# In[172]:


i = 1 
while i<11:
    print (i,"hellow world")  ## 1o times hellow world using while loop 
    i = i+1               


# ## function in python 

# In[173]:


alist = [11,12,14,15,25,147,66,4,3,2,4,5,6,98,7,40]


# In[174]:



    print(alist)


# In[175]:


alist.append(1000)
alist


# In[176]:


del(alist[-1])


# In[177]:


alist


# In[178]:



alist.remove(15)


# In[179]:


alist


# In[180]:


sorted(alist)      # sorted fucntion sort the list but does not change into sorted for permanent


# In[181]:


alist    # see 


# In[182]:



alist.sort()    # sort.() sort the list permanently 
alist


# In[183]:


alist   #see   


# In[184]:


len(alist)   # len function tells the length of the list or tuple


# In[185]:


alist = tuple(alist)


# In[186]:


alist   


# In[187]:


len(alist)


# In[188]:


sum(alist)


# In[189]:


alist = list(alist)


# In[190]:


alist


# In[191]:


sum(alist)    #  sum the function tells the total sum of list and tuple 


# In[192]:


t = -1200.50   # abs fuction gives the absolute value of the number 
h = +120.12     


# In[193]:


print(abs(t))    # abs actally fucntion example
abs(h)


# In[194]:


all(alist)     # all function give true if all item is iterable 


# In[195]:


# ascii function 
ascii(alist)


# In[196]:


# enumerate - takes the a collection (eg. a tuple) and gives it's enumerate object (iterable , start)

lis = ("ram","deepak","lamp","tahir")


# In[197]:


for x, items in enumerate(lis):
    print(x,items)


# In[198]:


user = ['tahir','deepak','suraj','gurmeet']            # format() function 
comp = ['dell','hp','dell','apple']
for i in range(0, len(user)):
               template = "compter used by {} is {}"
               print(template.format(user[i],comp[i]))


# In[199]:


id(lis)     # tells the unique id for each object 


# In[200]:


pow(2,4) # power function


# In[201]:


pow(10,0)


# In[202]:


pow(0,10)


# In[203]:


pow(4,2,1)


# ### user defined fuction by def 

# In[204]:


def function1():
    print("hellow python")     # simple defined function for hellow world 
function1()


# In[205]:


function1()
function1()
function1()
function1()


# In[206]:


def first1():
    a = int(input("enter first no.",))
    b = int(input("enter secound no.",))     #a simple user defined function
    y = a+b
    z = y/2
    print("sum of two numbers.",y)
    print("average of two no.",z)


# In[207]:


first1()    # function calling 
    


# In[208]:


def function2(country="India"):
    print("I am from",country)


# In[209]:


function2()


# In[210]:


function2('usa')
function2('Dubai')
function2('England')
function2('Saudi')


# In[211]:


a="india"
def fuctionc(a):
    print("I am from ",a)


# In[212]:


fuctionc(a)


# In[213]:


fuctionc("saudi")


# In[214]:


def mulp(x):
    return 5*x
print(mulp(3))
print(mulp(5))
mulp(8)


# In[215]:


"""this is the fuction based on pow of (a+b)"""
def squar(a,b):
    result = pow(a,2) + pow(b,2) + 2*a*b
    return result


# In[216]:


squar(2,3)


# In[217]:


squar(1,1)


# In[218]:


x = lambda a : a+10 # lambda function , one line functionality 


# In[219]:


print(x(20))
print(x(30))      # lambda function example 
print(x(90))


# In[220]:


u = lambda a:a*a*a # cube program using lambda function 
print(u(2))


# In[221]:


print(u(10))


# In[222]:


h = lambda a,b,c,d:a+b+c+d


# In[223]:


print(h(2,3,4,5))


# In[224]:


h(3,8,9,0)


# ## try and except in python

# In[225]:


x = int(input("enter the first no: "))
y = int(input("enter the secound no: "))           # exception handling , division by zero   # take a look at below programme
try:
    z = x/y
except Exception as e:    
    print("exception occured: ",e)                # if we don't know the name of exception then we use  (Exception as e)
    z = None
print("Division is: ",z)    
   


# In[228]:


x = int(input("enter the first no: "))
y = int(input("enter the secound no: "))           # relplace Exception as e by ZeroDivisionError(actual error)
try:
    z = x/y
except ZeroDivisionError:                          # now we know the name of the exception
    print("Division by zero exception ")
    z = None
print("Division is: ",z)    
   


# ### Objects and class 

# In[229]:


class Person:
    def __init__(self):
        self.name = "Jack"              #class and object in python 
        self.gender = "Male"
        self.age = 23
        self.weight = 85
    def talk(self):
        print("Hi I'm", self.name)
    def vote(self):
        if self.age<18:
            print("you can't vote Mr.", self.name)
        else:
            print("you can vote Mr.", self.name)
    def weight(self):
        if self.weight>80:
            print("you are over weight Mr.", self.name)
        else:
            print("you are fit and fine Mr.", self.name)
obj = Person()
Person.talk(obj)
Person.vote(obj)

Person.weight(obj)


# In[230]:


class Person:
    def __init__(self,n,g,a):
        self.name = n              # Here we will pass the varriable to this class and multiple object to the same class 
        self.gender = g
        self.age = a
    def talk(self):
        print("Hi I'm", self.name)
    def vote(self):
        if self.age<18:
            print("you can't vote Mr.", self.name)
        else:
            print("you can vote Mr.", self.name)
         
obj1 = Person("jack","male",27)
obj2 = Person("Rohan","male",12)
obj3 = Person("meera","female",18)

obj1.vote()
obj2.vote()
obj3.vote()

obj1.talk()
obj2.talk()
obj3.talk()



# In[231]:


class Employee:
    def __init__(self,naam,gr,umr,yrexp,cs):      # class for new hire employee ,,# my own creation 
        self.name = naam
        self.gender = gr
        self.age = umr
        self.yrexp = yrexp
        self.cs = cs
    def naam(self):
        print("we glad to have you Mr ",self.name)
        print("sex: ",self.gender)
    def gr(self):
        print(self.gender)
    def umr(self):
        r = 60-self.age
        print ("your current age is:- ",self.age)
        print (f"Mr {self.name} you will be retired after {r} years")
    def hike(self):
        if self.yrexp >= 2:
            print("egible for 20% hike on current salary")
        else:
            print("not egible for hike")
    def total_hike(self):
        h = 0.20*self.cs + self.cs
        print ("current salary: ",self.cs)
        print("salary after hike: ",h)
            


# In[232]:


tahir = Employee("Tahir","male",23,2,20000)


# In[233]:


tahir.naam()
tahir.gr()
tahir.hike()
tahir.umr()
tahir.total_hike()


# In[234]:


jeetu = Employee("jeetu","male",24,5,150000)


# In[235]:


jeetu.naam()
jeetu.gr()
jeetu.hike()
jeetu.umr()
jeetu.total_hike()


# In[ ]:




