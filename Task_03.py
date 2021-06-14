input= input("Please enter a string: ")
#input function
#defining dictionary
myDict={}
#Assigning letter count as value for respective letters
for itvar in input:
    myDict[itvar] = input.count(itvar)
#Using sorted, sorting values in dictionary with function lambda x
output=sorted(myDict.items(),key=lambda x: x[1],reverse=True)
#printing the output in required order
for i in output:
    print(i[0],'=',i[1])
