#########################
# Creating a dictionary #
#########################
myDictionary={"firstName":"Xavier","lastName":"Ochoa","age":45,"faculty":True,"height":1.77}
print(myDictionary)
print(myDictionary.keys())
print(myDictionary.values())

####################
# Accessing values #
####################
print(myDictionary["firstName"])
print(myDictionary["lastName"])
print("My name is {} {}".format(myDictionary["firstName"],myDictionary["lastName"]))

#################
# Adding values #
#################
myDictionary["title"]= "Assistant Professor"
myDictionary["department"]= "ECT"
myDictionary["courses"]=["BLA2","CogSci"]
print(myDictionary)

####################
# Replacing values #
####################
myDictionary["lastName"] ="Ochoa Chehab"
print(myDictionary)

#########################
# Check if a key exists #
#########################
if "weight" in myDictionary:
     print("We have information about the weight")
else:
    print("We do not have information about the weight")

###############################
# Iterate over the dictionary #
###############################
for key in myDictionary.keys():
    value = myDictionary[key]
    print("{} has value {}".format(key,value))



