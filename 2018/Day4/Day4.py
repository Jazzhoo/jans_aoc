
counter =0
listOfPasswords = []
#for i in range(109165,576723):
for i in range(109165,576723):
    ifIncreasing = True
    ifAdjacent = False
    ifGroup = 0
    for j in range (1, len(str(i))):
        if str(i)[j] < str(i)[j-1]: 
            ifIncreasing = False
            break
        if str(i)[j] == str(i)[j-1]: 
            ifAdjacent = True
            ifGroup+=1
    if ifIncreasing and ifAdjacent and ifGroup<2: 
        counter+=1
        print(i)
print("The number of possible passwords is:", counter)
##
            


        