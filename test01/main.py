from test01_contents.util import *
from test01_contents.Student import *
from test01_contents.SuperStudent import *

#===================================
#__name__
#===================================
#print(__name__) # => "__main__"
#util.py print(__name__) # => "util"
#SuperStudent.py print(__name__) # => "SuperStudent"


#===================================
#one line for loop example
#===================================
# 1 (for loop in for loop)
#listTest = [str(i) for j in range(3) for i in range(j * 3, (j + 1) * 3)]
#print(listTest)

# 2 (for + if)
#listTest = [str(j) for j in range(10) if j % 3 == 0]
#print(listTest)

# 3 (all + for)
#listTest = [3, 6, 9, 10]
#if all(e % 3 == 0 for e in listTest) :
    #print("all is % 3 == 0")
#else :
    #print("all isn't % 3 == 0")

#===================================
#static method example
#===================================
#SuperStudent.mystaticmethod()
#===================================


#===================================
#text format example
#===================================
#adj = input("enter adj : ")
#print(f"input adj is {adj}")
#===================================


#===================================
#function example
#===================================
#test01(10)
#test02("hahahaha")


#===================================
#class example
#===================================
#haha = Student()
#print(haha.value01)

#haha2 = SuperStudent()
#print(haha2.value01)
#print(haha2.value03)
#===================================


#===================================
#File Write example
#===================================
#stream = open("testtest.txt", "w")
#for i in range(0, 10):
    #if i % 3 == 0 : 
        #stream.write(str(i) + " % 3 == 0\n")
    #elif i % 3 == 1 :
        #stream.write(str(i) + " % 3 == 1\n")
    #else :
        #stream.write(str(i) + " % 3 == 2\n")
#stream.close()
#===================================

#===================================
#File Write example (with)
#===================================
#with open("testtest02.txt", 'w') as stream :
    #for i in range(0, 10) : 
        #stream.write(f"test {i}\n")
#===================================

#===================================
#File Read example
#===================================
#stream = open("testtest.txt", "r")
#print(stream.read())
#stream.close()
#===================================

#===================================
#File Read example (with)
#===================================
#with open("testtest02.txt", 'r') as stream :
    #print(stream.read())
#===================================