###################
# Creating a list #
###################
colors=['red','green','blue']
print(colors)

##################################
# Accessing an element in a list #
##################################
print(colors[0])
print(colors[2])

##############################
# Accessing a part of a list #
##############################
indices=['zero','one','two','three','four','five']
print(indices[2:4])
print(indices[2:])
print(indices[:4])

####################
# Negative indices #
####################
print(indices[-1])
print(indices[-2:])

######################
# Reassigning values #
######################
colors=['caramel','gold','silver','occur']
print(colors)
colors[1]="aureum"
print(colors)
colors[1:2]=["gold","argentine"]
print(colors)

#######################
# Iterating over list #
#######################
for i in [100,235,35]:
        if i%2==0:
               print("{} is even".format(i))
        else:
               print("{} is odd".format(i))

numbers=[8,25,32, 45, 29, 38, 66]
for i in numbers:
        if i%2==0:
               print("{} is even".format(i))
        else:
               print("{} is odd".format(i))

numberList= range(0,20)
print(numberList)
for i in numberList:
       if i%2==0:
              print("{} is even".format(i))
       else:
              print("{} is odd".format(i))

###########################
# Add elements at the end #
###########################
exampleList=["boat","home","family"]
print(exampleList)
exampleList.append("pencil")
exampleList.append("watch")
print(exampleList)

growingList =[]
print(growingList)
growingList.append(1)
growingList.append(25)
growingList.append(90)
print(growingList)

###############
# List Length #
###############
exampleList = ["student1","student2","student3","student4"]
print(len(exampleList))
print(len(exampleList[0]))


##########################
# Multidimensional Lists #
##########################
# a=[[1,2,3],[4,5,6],[7,8,9]]
# print(a)
# print(a[0][0])
# print(a[1][2])

####################################
# Iterating multidimensional lists #
####################################
# for i in range(0,len(a)):
#     for j in range(0,len(a[i])):
#         print(a[i][j])












